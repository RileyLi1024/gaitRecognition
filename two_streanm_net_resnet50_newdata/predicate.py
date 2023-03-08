import os

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from net.two_stream_net_resnet50 import TwoStreamNet_resnet50
from _utils.dataloader import GaitDataset
from torch.utils.data import DataLoader

def accuracy(out,label):
    #  记得reshape，确保preds和label的shape一样
    preds = torch.argmax(out,dim=1).reshape(-1,1) # 如果dim=1则返回每行的最大值

    a = (preds == label).float().mean()

    return a

if __name__ == '__main__':

    device = torch.device('cuda')
    net = TwoStreamNet_resnet50()
    net.load_state_dict(torch.load('./logs/Epoch1_train_loss0.5208228943408082_val_loss0.44838560699045027.pkl'))
    net.to(device)
    net.eval()

    root_dir1 = './data/data1'
    root_dir2 = './data/data2'

    # index = './data/训练文件_0425_person1-30_file0-2223.csv'
    # index = './data/测试文件_0425_person31-49_file2223-3792.csv'

    index = './data/测试文件_0508.CSV'
    train_dataset = GaitDataset(root_dir1, root_dir2, index)
    gen = DataLoader(train_dataset, shuffle=True, batch_size=64, num_workers=0, pin_memory=True,
                     drop_last=True)
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
        m = nn.Softmax(dim=1)
        softmax_out = m(out)
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
    #     print(float(softmax_out.data))