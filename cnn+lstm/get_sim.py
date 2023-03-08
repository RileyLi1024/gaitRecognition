import os

import torch
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

from net.cnn_lstm import CnnLstm

def csv2tensor(data1_path, data2_path):
    '''
    :param data1_path:
    :param data2_path:
    :return: 网络可以接受的数据格式
    '''

    data1_df = pd.read_csv(data1_path)
    data2_df = pd.read_csv(data2_path)

    """
    获取单个数据1 样本
    """
    data1_data_df = data1_df.iloc[:, 1:]
    data1_array = np.asarray(data1_data_df)
    data1 = torch.from_numpy(data1_array).type(torch.FloatTensor)
    data1 = torch.unsqueeze(data1, dim=0)
    """
    获
    取单个数据2 样本
    """
    data2_data_df = data2_df.iloc[:, 2:]
    data2_array = np.asarray(data2_data_df)
    data2 = torch.from_numpy(data2_array).type(torch.FloatTensor)
    data2 = torch.unsqueeze(data2, dim=0)
    data2 = torch.unsqueeze(data2, dim=0)

    return data1, data2

def get_feature(x, y):
    '''

    :param x: data1
    :param y: data2
    :return:
    '''
    data1 = x.to(device)
    data2 = y.to(device)
    out = net(data2, data1)
    feature = net.feature.cpu().data.numpy()

    return feature

def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)

    return float(num / denom)

data1_path_p1 = r'E:\workspace-sts\Gait\Matrix\video1\real_one.csv'
data2_path_p1 = r'E:\workspace-sts\Gait\Matrix\video2\real_two.csv'

data1_path_p2 = r'E:\workspace-sts\Gait\Matrix\video1\real_one.csv'
data2_path_p2 = r'E:\workspace-sts\Gait\Matrix\video2\real_two.csv'

# data1_path_p1 = r'G:\Wy\cnn+lstm\data\data1_test\data1_1.csv'

# data2_path_p1 = r'G:\Wy\cnn+lstm\data\data2_test\data2_1.csv'

# data1_path_p2 = r'G:\Wy\cnn+lstm\data\data1_test\data1_110.csv'

# data2_path_p2 = r'G:\Wy\cnn+lstm\data\data2_test\data2_110.csv'
# G:\Wy\cnn+lstm\data\data1_test
# G:\Wy\cnn+lstm\data\data1_test

data1_p1, data2_p1 = csv2tensor(data1_path_p1, data2_path_p1)
data1_p2, data2_p2 = csv2tensor(data1_path_p2, data2_path_p2)


# 加载网络
device = torch.device('cuda')
net = CnnLstm()
net.load_state_dict(torch.load(r'E:\workspace-sts\Gait\cnn+lstm\logs\98_0.2880191206932068.pkl'))
net.to(device)
net.eval()

feature_p1 = get_feature(data1_p1, data2_p1)
feature_p2 = get_feature(data1_p2, data2_p2)
# print(feature_p1)

sim = cosine_similarity(feature_p1,feature_p2)

print(sim)



