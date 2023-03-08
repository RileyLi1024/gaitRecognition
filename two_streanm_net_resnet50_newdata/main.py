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


def csv2tensor(data_spath_p1, data_tpath_p1,data_spath_p2, data_tpath_p2):
    '''
    :param data_spath_p1:
    :param data_tpath_p1:
    :param data_spath_p2:
    :param data_tpath_p2:
    :return: 网络可以接受的数据格式
    '''

    data1_1_df = pd.read_csv(data_spath_p1)   #读取p1的空间特征
    data2_1_df = pd.read_csv(data_tpath_p1)   #读取p1的时间特征
    data1_2_df = pd.read_csv(data_spath_p2)   #读取p2的空间特征
    data2_2_df = pd.read_csv(data_tpath_p2)   #读取p2的时间特征

    """
    将获取data1_1数据转换为网络可识别的数据
    """
    data1_1_data_df = data1_1_df.iloc[:,1:]
    data1_1_array = np.asarray(data1_1_data_df)
    data1_1 = torch.from_numpy(data1_1_array).type(torch.FloatTensor)    #numpy转为tensor
    data1_1 = torch.unsqueeze(data1_1,dim=0)   #相当于batch_size设为1
    # print(data1_name)

    """
    将获取data1_2数据转换为网络可识别的数据
    """
    data1_2_data_df = data1_2_df.iloc[:, 1:]
    data1_2_array = np.asarray(data1_2_data_df)
    data1_2 = torch.from_numpy(data1_2_array).type(torch.FloatTensor)
    data1_2 = torch.unsqueeze(data1_2,dim=0)    #相当于batch_size设为1
    """
    将获取data2_1数据转换为网络可识别的数据
    """
    # data2_1_data_df = data2_1_df.iloc[:, 3:]#之前数据处理方式
    data2_1_data_df = data2_1_df.iloc[:, 2:48]#第二次数据处理方式
    data2_1_array = np.asarray(data2_1_data_df)
    data2_1 = torch.from_numpy(data2_1_array).type(torch.FloatTensor)
    data2_1 = torch.unsqueeze(data2_1, dim=0)
    data2_1 = torch.unsqueeze(data2_1,dim=0)    #相当于batch_size设为1
    # print(data2_name)
    """
    将获取data2_2数据转换为网络可识别的数据
    """
    # data2_2_data_df = data2_2_df.iloc[:, 3:]#之前数据处理方式
    data2_2_data_df = data2_2_df.iloc[:, 2:48]#第二次数据处理方式
    data2_2_array = np.asarray(data2_2_data_df)
    data2_2 = torch.from_numpy(data2_2_array).type(torch.FloatTensor)
    data2_2 = torch.unsqueeze(data2_2, dim=0)
    data2_2 = torch.unsqueeze(data2_2, dim=0)   #相当于batch_size设为1
    return data1_1,data1_2,data2_1,data2_2


if __name__ == '__main__':

    device = torch.device('cuda')
    net = TwoStreamNet_resnet50()
    net.load_state_dict(torch.load('E:/user/lj/two_streanm_net_resnet50_newdata/logs/Epoch1_train_loss0.5208228943408082_val_loss0.44838560699045027.pkl'))    #加载模型
    net.to(device)
    net.eval()

    # root_dir1 = './data/data1'
    # root_dir2 = './data/data2'

    # index = './data/训练文件_0425_person1-30_file0-2223.csv'
    # index = './data/测试文件_0425_person31-49_file2223-3792.csv'

    # index = './data/测试文件_0508.CSV'
    # train_dataset = GaitDataset(root_dir1, root_dir2, index)
    # gen = DataLoader(train_dataset, shuffle=True, batch_size=64, num_workers=0, pin_memory=True,
    #                  drop_last=True)

    #读取特征矩阵
    data_spath_p1 = r'E:\workspace-sts\Gait\Matrix\video1\real_one.csv'
    data_tpath_p1 = r'E:\workspace-sts\Gait\Matrix\video1\real_two.csv'

    data_spath_p2 = r'E:\workspace-sts\Gait\Matrix\video2\real_one.csv'
    data_tpath_p2 = r'E:\workspace-sts\Gait\Matrix\video2\real_two.csv'
 
    datas_p1,datas_p2, datat_p1,datat_p2 = csv2tensor(data_spath_p1, data_tpath_p1,data_spath_p2, data_tpath_p2)   #将特征矩阵转化为tensor
    data1_p1 = datas_p1.to(device)
    data1_p2 = datas_p2.to(device)
    data2_p1 = datat_p1.to(device)
    data2_p2 = datat_p2.to(device)
    # out = net(data1_p1, data1_p2,data2_p1, data2_p2)
    out = net(data2_p1, data2_p2, data1_p1, data1_p2)    #调用网络模型
    preds = torch.argmax(out,dim=1).reshape(-1,1) #  获取判别结果，1为是一个人，0为不是一个人
    result = preds.cpu().numpy()
    print(result.reshape(-1)[0])
    # for i, data in enumerate(gen):
    #     total_loss = 0
    #     data1_1, data1_2, data2_1, data2_2, label = data[0], data[1], data[2], data[3], data[4]

    #     data1_1 = data1_1.to(device)
    #     data1_2 = data1_2.to(device)
    #     data2_1 = data2_1.to(device)
    #     data2_2 = data2_2.to(device)
    #     label = label.to(device, dtype=torch.int64)

    #     # print(label1.cpu().numpy())

    #     out = net(data2_1, data2_2, data1_1, data1_2)
    #     m = nn.Softmax(dim=1)
    #     softmax_out = m(out)
    #     accuracy_ = accuracy(out,label)
    #     accuracy_total+=accuracy_.item()
    #     # a, pred = torch.max(out, 1)
    #     # pred_reshape = pred.reshape(-1, 1)
    #     # a = (pred == label)
    #     # correct += (pred_reshape == label).sum().item()
    #     # total += label.size(0)
    #     # accuracy = float(correct) / total
    #     print(accuracy_total/(i+1))
        # print(i)
        # print(out)
    # out = net(data2_1, data2_2, data1_1, data1_2)
    #     print(float(softmax_out.data))