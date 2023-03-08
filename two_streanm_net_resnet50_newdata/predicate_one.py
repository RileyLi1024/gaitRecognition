import os

import numpy as np
import pandas as pd
from net.two_stream_net import TwoStreamNet,TwoStreamNet2_bn
import torch
import torch.nn as nn
from net.two_stream_net_resnet50 import TwoStreamNet_resnet50
device = torch.device('cuda')
net = TwoStreamNet_resnet50()

net.load_state_dict(torch.load(r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net_resnet50\two_stream_net\logs\two_stream_net_resnet50\Epoch7_train_loss0.09674956450332316_val_loss3.818527543732009.pkl'))
net.to(device)
net.eval()

root = r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net_resnet50\two_stream_net\data\第二方案数据更新\覆盖后样本'
data1_root = os.path.join(root, 'data1')
data2_root = os.path.join(root, 'data2')

def accuracy(out,label):
    #  记得reshape，确保preds和label的shape一样
    preds = torch.argmax(out,dim=1).reshape(-1,1) # 如果dim=1则返回每行的最大值

    a = (preds == label).float().mean()

    return a
def read_data(data1,data2):
    data1_1_df = pd.read_csv(os.path.join(data1_root,'data1_{}.csv'.format(data1)))
    data1_2_df = pd.read_csv(os.path.join(data1_root, 'data1_{}.csv'.format(data2)))

    data2_1_df = pd.read_csv(os.path.join(data2_root, 'data2_{}.csv'.format(data1)))
    data2_2_df = pd.read_csv(os.path.join(data2_root, 'data2_{}.csv'.format(data2)))

    data1_1_data_df = data1_1_df.iloc[:, 3:]
    data1_1_array = np.asarray(data1_1_data_df)
    data1_1 = torch.from_numpy(data1_1_array).type(torch.FloatTensor)
    data1_1 = torch.unsqueeze(data1_1, dim=0)

    data1_2_data_df = data1_2_df.iloc[:, 3:]
    data1_2_array = np.asarray(data1_2_data_df)
    data1_2 = torch.from_numpy(data1_2_array).type(torch.FloatTensor)
    data1_2 = torch.unsqueeze(data1_2, dim=0)

    data2_1_data_df = data2_1_df.iloc[:, 3:]
    data2_1_array = np.asarray(data2_1_data_df)
    data2_1 = torch.from_numpy(data2_1_array).type(torch.FloatTensor)
    data2_1 = torch.unsqueeze(data2_1, dim=0)
    data2_1 = torch.unsqueeze(data2_1, dim=0)

    data2_2_data_df = data2_2_df.iloc[:, 3:]
    data2_2_array = np.asarray(data2_2_data_df)
    data2_2 = torch.from_numpy(data2_2_array).type(torch.FloatTensor)
    data2_2 = torch.unsqueeze(data2_2, dim=0)
    data2_2 = torch.unsqueeze(data2_2, dim=0)


    return data1_1,data1_2,data2_1,data2_2
if __name__ == '__main__':

    from _utils.dataloader import GaitDataset

    root_dir1 = r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net_resnet50\two_stream_net\data\第二方案数据更新\覆盖后样本\data1'
    root_dir2 = r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net_resnet50\two_stream_net\data\第二方案数据更新\覆盖后样本\data2'

    train_index = r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net_resnet50\two_stream_net\data\第二方案数据更新\测试文件0131.csv'
    # val_index = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\sample\val_no4845_sample.csv'
    data1_1, data1_2, data2_1, data2_2 = same_or_not(1,2)
    data1_1 = data1_1.to(device)
    data1_2 = data1_2.to(device)
    data2_1 = data2_1.to(device)
    data2_2 = data2_2.to(device)
    out = net(data2_1, data2_2, data1_1, data1_2)
    m = nn.Softmax(dim=1)
    out_softmax = m(out)

    from torch.utils.data import DataLoader
    train_dataset = GaitDataset(root_dir1, root_dir2, train_index)
    gen = DataLoader(train_dataset, shuffle=True, batch_size=32, num_workers=0, pin_memory=True,
                     drop_last=True)
    # label = label.to(device, dtype=torch.int64)

    # print(label1.cpu().numpy())
    # optimizer.zero_grad()
    correct = 0
    total =0
    accuracy_total = 0
    for i, data in enumerate(gen):
        total_loss = 0
        data1_1, data1_2, data2_1, data2_2, label = data[0], data[1], data[2], data[3], data[4]

        data1_1 = data1_1.to(device)
        data1_2 = data1_2.to(device)
        data2_1 = data2_1.to(device)
        data2_2 = data2_2.to(device)
        label = label.to(device, dtype=torch.int64)

        # print(label1.cpu().numpy())

        out = net(data2_1, data2_2, data1_1, data1_2)
        accuracy_ = accuracy(out,label)
        accuracy_total+=accuracy_.item()
        # a, pred = torch.max(out, 1)
        # pred_reshape = pred.reshape(-1, 1)
        # a = (pred == label)
        # correct += (pred_reshape == label).sum().item()
        # total += label.size(0)
        # accuracy = float(correct) / total
        print(accuracy_total/(i+1))
        # print(i)
        # print(out)
    # out = net(data2_1, data2_2, data1_1, data1_2)
    print(out)