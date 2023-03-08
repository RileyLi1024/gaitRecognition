import os
import numpy as np
import time
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.backends.cudnn as cudnn

from torch.utils.data import DataLoader

from net.cnn_lstm import CnnLstm, Lstm, Fc
from PIL import Image
from torchsummary import summary
from _utils.dataloader import GaitDataset

pre_train = False
device = torch.device('cuda')
root_dir1 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data1_train'
root_dir2 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data2_train'

test_root_dir1 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data1_test'
test_root_dir2 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data2_test'

Batch_size = 64
LR = 0.001

# model = CnnLstm()
# model.to(device)
# # summary(model,(50,45))
# data2 = torch.FloatTensor(1,1,50,45).to(device)
# out_cnn = model(data2)
# print("out_cnn:",out_cnn.shape)
#
#
# model_lstm = Lstm()
# model_lstm.to(device)
# # summary(model_lstm, (51, 1, 44))
# data = torch.FloatTensor(1,51, 45)
# data = data.to(device)
# # data
# out_lstm = model_lstm(data)
# print(out_lstm[0].shape)
# out_cnn_fla = out_cnn.view(1,-1)
# out_lstm_fla = out_lstm[0].view(1,-1)
# out_cat = torch.cat([out_cnn_fla,out_lstm_fla],dim=1)
#
#
# model_fc = Fc()
# model_fc.to(device)
# out_fin = model_fc(out_cat)


net = CnnLstm()
if pre_train:
    net.load_state_dict(torch.load(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\logs\52_0.004203313961625099.pkl'))
net.to(device)
print(net)
# data1 = torch.FloatTensor(1,51, 45).to(device)
# data2 = torch.FloatTensor(1,1,50,45).to(device)
# out = model(data2,data1)

train_dataset = GaitDataset(root_dir1, root_dir2)
test_dataset = GaitDataset(test_root_dir1, test_root_dir2)

# data1,data2,label1,label2 = train_dataset[1]

# out = model(data2,data1)


gen = DataLoader(train_dataset, shuffle=True, batch_size=Batch_size, num_workers=0, pin_memory=True,
                 drop_last=True)
test_gen = DataLoader(test_dataset, shuffle=True, batch_size=512, num_workers=0, pin_memory=True,
                      drop_last=True)

criterion = nn.CrossEntropyLoss()
# criterion = nn.SOFTMAX()
# optimizer = optim.SGD(net.parameters(), lr=LR, momentum=0.9)
optimizer = optim.Adam(net.parameters(), LR)

loss = 0.0
for epoch in range(100):

    for i, data in enumerate(gen):
        total_loss = 0
        data1, data2, label1, label2 = data[0], data[1], data[2], data[3]

        data1 = data1.to(device)
        data2 = data2.to(device)
        label1 = label1.to(device, dtype=torch.int64)
        # print(label1.cpu().numpy())
        optimizer.zero_grad()
        out = net(data2, data1)
        loss = criterion(out.squeeze(), label1.squeeze())
        loss.backward()
        optimizer.step()
        total_loss += loss
        print('[Epoch %d, Batch %5d] loss: %.3f' %
              (epoch + 1, i + 1, total_loss / (i + 1)))


    print("开始验证")
    for i, data in enumerate(test_gen):
        total_loss = 0
        data1, data2, label1, label2 = data[0], data[1], data[2], data[3]

        data1 = data1.to(device)
        data2 = data2.to(device)
        label1 = label1.to(device, dtype=torch.int64)
        # print(label1.cpu().numpy())
        optimizer.zero_grad()
        out = net(data2, data1)
        loss = criterion(out.squeeze(), label1.squeeze())
        loss.backward()
        optimizer.step()
        total_loss += loss
    print("test_loss = {}".format(total_loss / (i + 1)))
    torch.save(net.state_dict(), './logs/{}_{}.pkl'.format(epoch, total_loss / (i + 1)))
