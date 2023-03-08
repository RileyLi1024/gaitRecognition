import os

import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import sys
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


def get_feature(s_matrix_path, t_matrix_path, path3):
    '''

    :param s_matrix_path: spatial matrix
    :param t_matrix_path: t      matrix
    :return:
    '''
    s_matrix, t_matrix = csv2tensor(s_matrix_path, t_matrix_path)

    # 加载网络
    device = torch.device('cuda')
    net = CnnLstm()
    net.load_state_dict(torch.load(r'E:\user\lj\cnn+lstm\logs\98_0.2880191206932068.pkl'))
    net.to(device)
    net.eval()

    s_matrix = s_matrix.to(device)
    t_matrix = t_matrix.to(device)
    out = net(t_matrix, s_matrix)
    feature = net.feature.cpu().data.numpy()
    print(feature)
    np.savetxt(path3, feature, fmt='%f', delimiter=',')



if __name__ == '__main__':
    username = sys.argv[1]
    name = sys.argv[2]
    if username == "":
        path1 = "E:\\workspace-sts\\Gait\\Matrix\\video2\\real_one.csv"
        path2 = "E:\\workspace-sts\\Gait\\Matrix\\video2\\real_two.csv"
        path3 = "E:\\workspace-sts\\Gait\\Matrix\\video2\\matrix2.txt"
    else:
        path1 = "E:\\workspace-sts\\Gait\\Register\\" + username + "\\" + name + "\\real_one.csv"
        path2 = "E:\\workspace-sts\\Gait\\Register\\" + username + "\\" + name + "\\real_two.csv"
        txt_name = "matrix1_" + username + "_" + name + ".txt"
        path3 = "E:\\workspace-sts\\Gait\\Register\\" + txt_name
    # parser = argparse.ArgumentParser()
    # parser.add_argument('s_matrix_path', type=str, default="E:\Gait-System\Gait-zhangdi\Matrix\video1\real_one.csv")
    # parser.add_argument('t_matrix_path', type=str, default="E:\Gait-System\Gait-zhangdi\Matrix\video1\real_two.csv")
    # args = parser.parse_args()
    s_matrix_path = path1
    t_matrix_path = path2
    get_feature(s_matrix_path, t_matrix_path, path3)

# data1_path_p1 = r'E:\3DhumanPose-GPU\Gait-zhangdi\Matrix\video1\real_one.csv'
# data2_path_p1 = r'E:\3DhumanPose-GPU\Gait-zhangdi\Matrix\video1\real_two.csv'

# data1_path_p2 = r'E:\3DhumanPose-GPU\Gait-zhangdi\Matrix\video2\real_one.csv'
# data2_path_p2 = r'E:\3DhumanPose-GPU\Gait-zhangdi\Matrix\video2\real_two.csv'

# data1_path_p1 = r'G:\Wy\cnn+lstm\data\data1_test\data1_1.csv'

# data2_path_p1 = r'G:\Wy\cnn+lstm\data\data2_test\data2_1.csv'

# data1_path_p2 = r'G:\Wy\cnn+lstm\data\data1_test\data1_110.csv'

# data2_path_p2 = r'G:\Wy\cnn+lstm\data\data2_test\data2_110.csv'
# G:\Wy\cnn+lstm\data\data1_test
# G:\Wy\cnn+lstm\data\data1_test

# data1_p1, data2_p1 = csv2tensor(data1_path_p1, data2_path_p1)
# data1_p2, data2_p2 = csv2tensor(data1_path_p2, data2_path_p2)


# # 加载网络
# device = torch.device('cuda')
# net = CnnLstm()
# net.load_state_dict(torch.load(r'G:\Wy\cnn+lstm\logs\98_0.2880191206932068.pkl'))
# net.to(device)
# net.eval()

# feature_p1 = get_feature(data1_p1, data2_p1)
# feature_p2 = get_feature(data1_p2, data2_p2)

# sim = cosine_similarity(feature_p1,feature_p2)

# print(sim)
