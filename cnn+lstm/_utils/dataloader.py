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
    def __init__(self, root_dir1, root_dir2):
        super(GaitDataset, self).__init__()

        self.root_dir1 = root_dir1
        self.root_dir2 = root_dir2
        self.file_list1 = os.listdir(root_dir1)
        self.file_list2 = os.listdir(root_dir2)

    def __len__(self):
        return len(self.file_list1)

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
        data1_name = os.path.join(self.root_dir1, self.file_list1[index])
        data1_df = pd.read_csv(data1_name)
        data2_name = os.path.join(self.root_dir2, self.file_list2[index])
        data2_df = pd.read_csv(data2_name)
        """
        获取单个数据1 样本
        """
        data1_data_df = data1_df.iloc[:,3:]
        data1_array = np.asarray(data1_data_df)
        data1 = torch.from_numpy(data1_array).type(torch.FloatTensor)
        # data1 = torch.unsqueeze(data1,dim=0)
        # print(data1_name)

        """
        获取单个数据1 标签
        """
        data1_label_df = data1_df.iloc[:,:1]
        data1_label = data1_label_df.iloc[0,0]
        data1_label = np.array((data1_label[:3]),dtype=np.float64).reshape(-1)
        data1_label = torch.from_numpy(data1_label).type(torch.FloatTensor)
        # print(data1_label)
        """
        获取单个数据2 样本
        """
        data2_data_df = data2_df.iloc[:,3:]
        data2_array = np.asarray(data2_data_df)
        data2 = torch.from_numpy(data2_array).type(torch.FloatTensor)
        data2 = torch.unsqueeze(data2, dim=0)
        # print(data2_name)

        """
        获取单个数据2 标签
        """
        data2_label_df = data2_df.iloc[:, :1]
        data2_label = data2_label_df.iloc[0, 0]
        data2_label = np.array((data2_label[:3]), dtype=np.float64).reshape(-1)
        data2_label = torch.from_numpy(data2_label).type(torch.FloatTensor)

        return data1,data2,data1_label,data2_label
