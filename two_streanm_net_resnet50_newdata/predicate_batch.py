import os

import numpy as np
import pandas as pd
from net.two_stream_net import TwoStreamNet,TwoStreamNet2_bn
import torch
from tqdm import tqdm
import torch.nn as nn

from net.two_stream_net_resnet50 import TwoStreamNet_resnet50

# 开集测试
root = './data'
data1_root = os.path.join(root, 'data1')
data2_root = os.path.join(root, 'data2')

#闭集测试
# root = r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net\data'
# data1_root = os.path.join(root, 'data1_whole')
# data2_root = os.path.join(root, 'data2_whole')
def accuracy(out,label):
    #  记得reshape，确保preds和label的shape一样
    preds = torch.argmax(out,dim=1).reshape(-1,1) # 如果dim=1则返回每行的最大值

    preds = torch.argmax(out, dim=1).reshape(-1, 1)
    a = (preds == label).float().mean()

    return a
def same_or_not(data1,data2):
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

    data2_1_data_df = data2_1_df.iloc[:, 3:49]
    data2_1_array = np.asarray(data2_1_data_df)
    data2_1 = torch.from_numpy(data2_1_array).type(torch.FloatTensor)
    data2_1 = torch.unsqueeze(data2_1, dim=0)
    data2_1 = torch.unsqueeze(data2_1, dim=0)

    data2_2_data_df = data2_2_df.iloc[:, 3:49]
    data2_2_array = np.asarray(data2_2_data_df)
    data2_2 = torch.from_numpy(data2_2_array).type(torch.FloatTensor)
    data2_2 = torch.unsqueeze(data2_2, dim=0)
    data2_2 = torch.unsqueeze(data2_2, dim=0)

    return data1_1,data1_2,data2_1,data2_2

if __name__ == '__main__':
    device = torch.device('cuda')
    net = TwoStreamNet_resnet50()

    net.load_state_dict(torch.load('./logs/Epoch0_train_loss0.604731774535201_val_loss0.3857733865026545.pkl'))
    net.to(device)
    net.eval()
    # _TEM_testxlsx_to_index(r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net\data\sample\test_no4845_sample.csv')
    index_file_path = './data/测试文件_0508.CSV'
    index = pd.read_csv(index_file_path)

    from _utils.dataloader import GaitDataset

    # root_dir1 = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\data1_whole'
    # root_dir2 = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\data2_whole'
    #
    # train_index = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\sample\openset_test.csv'
    # val_index = r'C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\sample\val_no4845_sample.csv'


    for index_num in tqdm(index.iterrows()):
        # data1_1, data1_2, data2_1, data2_2 = same_or_not(6344,6346)
        data1_1, data1_2, data2_1, data2_2 = same_or_not(index_num[1]['FILE1'].split('_')[1], index_num[1]['FILE11'].split('_')[1])

        data1_1 = data1_1.to(device)
        data1_2 = data1_2.to(device)
        data2_1 = data2_1.to(device)
        data2_2 = data2_2.to(device)

        out = net(data2_1, data2_2, data1_1, data1_2)

        m = nn.Softmax(dim=1)
        out_softmax = np.array(m(out).data.cpu())

        out_fin = np.array([index_num[0], index_num[1], out_softmax[0][0],out_softmax[0][1]])
        with open('./result/Open_Set_test.txt', 'a+') as f:
            # f.write(out_fin)
            # f.write('\n')
            f.write(str(index_num[1]['FLAG1']))
            f.write(',')
            f.write(str(index_num[1]['FLAG2']))
            f.write(',')
            f.write(str(index_num[1]['FILE1'].split('_')[1]))
            f.write(',')
            f.write(str(index_num[1]['FILE11'].split('_')[1]))
            f.write(',')
            f.write(str(out_softmax[0][0]))
            f.write(',')
            f.write(str(out_softmax[0][1]))
            f.write('\n')