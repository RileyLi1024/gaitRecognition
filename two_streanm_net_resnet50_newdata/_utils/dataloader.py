from random import shuffle
import numpy as np
import torch
import torch.nn as nn
import math
import torch.nn.functional as F
from PIL import Image
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
import os
import torchvision.transforms as transforms
import pandas as pd


class GaitDataset(Dataset):
    def __init__(self, root_dir1, root_dir2, root_train_index):
        super(GaitDataset, self).__init__()

        self.root_dir1 = root_dir1
        self.root_dir2 = root_dir2
        self.root_train_index = root_train_index
        self.file_list1 = os.listdir(root_dir1)
        self.file_list2 = os.listdir(root_dir2)
        self.train_index_df = pd.read_csv(self.root_train_index)
    def __len__(self):
        return len(self.train_index_df)

    def __getitem__(self, index):

        # """
        # 标签的处理
        # """
        # for mor in lines[1:]:
        #     y = np.array(mor.strip()).astype(np.float).reshape(-1)
        # y = torch.from_numpy(y)
        #
        # tmp_targets = np.array(y, dtype=np.float32)
        # 返回了最终处理好的图片和标签
        '''
        读取train.csv,已经写好了data1的读取，读取为df格式。
        '''


        data1_1_name = self.train_index_df.iloc[index, 3]+'.csv'
        data1_1_path = os.path.join(self.root_dir1, self.file_list1[self.file_list1.index(data1_1_name)])
        data1_1_df = pd.read_csv(data1_1_path)

        data1_2_name = self.train_index_df.iloc[index, 4]+'.csv'
        data1_2_path = os.path.join(self.root_dir1, self.file_list1[self.file_list1.index(data1_2_name)])
        data1_2_df = pd.read_csv(data1_2_path)

        data2_1_name = self.train_index_df.iloc[index, 5] + '.csv'
        data2_1_path = os.path.join(self.root_dir2, self.file_list2[self.file_list2.index(data2_1_name)])
        data2_1_df = pd.read_csv(data2_1_path)

        data2_2_name = self.train_index_df.iloc[index, 6] + '.csv'
        data2_2_path = os.path.join(self.root_dir2, self.file_list2[self.file_list2.index(data2_2_name)])
        data2_2_df = pd.read_csv(data2_2_path)

        # data1_name = os.path.join(self.root_dir1, self.file_list1[index])
        # data1_df = pd.read_csv(data1_name)
        # data2_name = os.path.join(self.root_dir2, self.file_list2[index])
        # data2_df = pd.read_csv(data2_name)
        """
        将获取data1_1数据转换为网络可识别的数据
        """
        data1_1_data_df = data1_1_df.iloc[:,3:]
        data1_1_array = np.asarray(data1_1_data_df)
        data1_1 = torch.from_numpy(data1_1_array).type(torch.FloatTensor)
        # data1 = torch.unsqueeze(data1,dim=0)
        # print(data1_name)

        """
        将获取data1_2数据转换为网络可识别的数据
        """
        data1_2_data_df = data1_2_df.iloc[:, 3:]
        data1_2_array = np.asarray(data1_2_data_df)
        data1_2 = torch.from_numpy(data1_2_array).type(torch.FloatTensor)

        """
        将获取data2_1数据转换为网络可识别的数据
        """
        # data2_1_data_df = data2_1_df.iloc[:, 3:]#之前数据处理方式
        data2_1_data_df = data2_1_df.iloc[:, 3:49]#第二次数据处理方式
        data2_1_array = np.asarray(data2_1_data_df)
        data2_1 = torch.from_numpy(data2_1_array).type(torch.FloatTensor)
        data2_1 = torch.unsqueeze(data2_1, dim=0)
        # print(data2_name)
        """
        将获取data2_2数据转换为网络可识别的数据
        """
        # data2_2_data_df = data2_2_df.iloc[:, 3:]#之前数据处理方式
        data2_2_data_df = data2_2_df.iloc[:, 3:49]#第二次数据处理方式
        data2_2_array = np.asarray(data2_2_data_df)
        data2_2 = torch.from_numpy(data2_2_array).type(torch.FloatTensor)
        data2_2 = torch.unsqueeze(data2_2, dim=0)

        """
        获取标签
        """
        label = self.train_index_df.iloc[index, 7]
        label = torch.tensor(label).type(torch.FloatTensor).reshape(-1)
        # """
        # 获取单个数据1 标签
        # """
        # data1_label_df = data1_df.iloc[:,:1]
        # data1_label = data1_label_df.iloc[0,0]
        # data1_label = np.array((data1_label[:3]),dtype=np.float64).reshape(-1)
        # data1_label = torch.from_numpy(data1_label).type(torch.FloatTensor)
        # print(data1_label)

        # """
        # 获取单个数据2 标签
        # """
        # data2_label_df = data2_df.iloc[:, :1]
        # data2_label = data2_label_df.iloc[0, 0]
        # data2_label = np.array((data2_label[:3]), dtype=np.float64).reshape(-1)
        # data2_label = torch.from_numpy(data2_label).type(torch.FloatTensor)

        # data1_1和data1_2送入lstm，data2_1和data2_2送入cnn，label是0或者1
        return data1_1, data1_2, data2_1, data2_2, label

# if __name__ == '__main__':
#     root_dir1 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data1_train'
#     root_dir2 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data2_train'
#     train_index = r'G:\Code\tf2_torch\pytorch\2_Projects\QYJ\two_stream_net\data\train.csv'
#     train_dataset = GaitDataset(root_dir1, root_dir2, train_index)
#     train_dataset[0]