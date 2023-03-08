import os
import numpy as np
import time
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.backends.cudnn as cudnn
from tqdm import tqdm
from torch.utils.data import DataLoader

from net.two_stream_net_resnet50 import TwoStreamNet_resnet50
from PIL import Image
from torchsummary import summary
from _utils.dataloader import GaitDataset

def loss_batch(model, loss_func, data2_1, data2_2, data1_1, data1_2, y, opt=None):
    out = model(data2_1, data2_2, data1_1, data1_2)

    # loss = loss_func(out.squeeze(), y.squeeze())
    loss = loss_func(out.reshape(len(data2_1),-1), y.squeeze())

    if opt is not None:
        loss.backward()  # 计算一次反向传播中的梯度
        opt.step()  # 应用计算的反向传播
        opt.zero_grad()  # 清空反向传播过程中计算的梯度
    return loss.item(), len(data2_1)

def fit_one_epoch(epoch, model, loss_func, opt, train_dl, valid_df):
    for epoch in range(epoch):
        model.train()
        train_loss = 0
        val_loss = 0
        i_train = 0
        for i, data in tqdm(enumerate(train_dl)):
            i_train = i
            data1_1, data1_2, data2_1, data2_2, label = data[0], data[1], data[2], data[3], data[4]
            data1_1 = data1_1.to(device)
            data1_2 = data1_2.to(device)
            data2_1 = data2_1.to(device)
            data2_2 = data2_2.to(device)
            label = label.to(device, dtype=torch.int64)

            train_losses, train_nums = loss_batch(net, loss_func, data2_1, data2_2, data1_1, data1_2, label, opt)
            # train_loss = (train_loss + train_losses) / 32
            train_loss = train_loss + train_losses
            # print('total_loss:', train_loss ,"i:",i+1)
            print('train_losses:', train_loss/(i+1))
        print("开始验证")
        model.eval()
        with torch.no_grad():
            for i, data in enumerate(valid_df):
                data1_1, data1_2, data2_1, data2_2, label = data[0], data[1], data[2], data[3], data[4]
                data1_1 = data1_1.to(device)
                data1_2 = data1_2.to(device)
                data2_1 = data2_1.to(device)
                data2_2 = data2_2.to(device)
                label = label.to(device, dtype=torch.int64)
                print(len(valid_df))
                val_losses, val_nums = loss_batch(net, loss_func, data2_1, data2_2, data1_1, data1_2, label)
                val_loss = (val_loss + val_losses)
                print("val_loss:", val_loss / (i+1))
        # train_loss = np.sum(np.multiply(train_losses, train_nums)) / np.sum(train_nums)

        torch.save(net.state_dict(), './logs/Epoch{}_train_loss{}_val_loss{}.pkl'.format(epoch, train_loss/ (i_train+1), val_loss/ (i+1)))


if __name__ == '__main__':
    EPOCH = 1000
    pre_train = True
    device = torch.device('cuda')


    root_dir1 = './data/data1'
    root_dir2 = './data/data2'

    train_index = './data/data0425_前49人_正样本太多/训练文件_0425_person1-30_file0-2223.csv'
    val_index = './data/data0425_前49人_正样本太多/训练文件_0425_person1-30_file0-2223.csv'

    # root_dir1 = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\data1_whole'
    # root_dir2 = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\data2_whole'
    #
    # train_index = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\sample\train_no4845_sample.csv'
    # val_index = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\sample\test_no4845_sample.csv'

    Batch_size = 128

    LR = 0.001
    net = TwoStreamNet_resnet50()

    if pre_train:
        net.load_state_dict(torch.load('./logs/Epoch1_train_loss0.5208228943408082_val_loss0.44838560699045027.pkl'))
    net.to(device)

    # print(net)
    # data1 = torch.FloatTensor(1,51, 45).to(device)
    # data2 = torch.FloatTensor(1,1,50,45).to(device)
    # out = model(data2,data1)

    train_dataset = GaitDataset(root_dir1, root_dir2, train_index)
    test_dataset = GaitDataset(root_dir1, root_dir2, val_index)

    # data1,data2,label1,label2 = train_dataset[1]

    # out = model(data2,data1)


    gen = DataLoader(train_dataset, shuffle=True, batch_size=Batch_size, num_workers=0, pin_memory=True,
                     drop_last=True)
    test_gen = DataLoader(test_dataset, shuffle=True, batch_size=Batch_size, num_workers=0, pin_memory=True,
                          drop_last=True)

    criterion = nn.CrossEntropyLoss()

    # optimizer = optim.SGD(net.parameters(), lr=LR, momentum=0.9)
    optimizer = optim.Adam(net.parameters(), LR)

    fit_one_epoch(epoch=EPOCH, model=net, loss_func=criterion, opt=optimizer, train_dl=gen, valid_df=test_gen)

