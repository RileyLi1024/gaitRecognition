import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from net.resnet50 import Bottleneck,ResNet

class TwoStreamNet_resnet50(nn.Module):
    '''
    第二次数据的模型，data2相比之前的数据，每个samle少了3列
    '''
    def __init__(self):
        super(TwoStreamNet_resnet50, self).__init__()

        self.resnet50 = ResNet(Bottleneck, [3, 4, 6, 3])

        self.lstm1 = nn.LSTM(input_size=88, hidden_size=64, batch_first=True)

        self.fc1 = nn.Linear(7296, 128)# out128
        self.fc2 = nn.Linear(128, 2)
        self.feature = []
        self.feature2 = []

    def forward(self, x1, x2, y1, y2):
        '''

        :param x1: cnn1
        :param x2: cnn2
        :param y1: lstm1
        :param y2: lstm2
        :return:
        '''
        # x1 = x1.unsqueeze(1)
        # x2 = x2.unsqueeze(1)
        # y1 = y1.

        x = torch.cat((x1, x2), 1)   # 按通道拼接cnn1和cnn2，cnn1[b,1,50,45]+cnn2[b,1,50,45]->[b,2,50,45]
        y = torch.cat((y1, y2), 2)    # 按特征拼接lstm1和lstm2，lstm1[b,50,44]+lstm2[b,50,44]->[b,50,88]

        g = self.resnet50(x)
        # x = F.leaky_relu(self.bn1(self.conv1(x)), 0.33)
        # x = self.pool(x)
        # x = self.dropout(x)
        # x = F.leaky_relu(self.bn2(self.conv2(x)), 0.33)
        # x = self.pool(x)
        # self.feature2 = x
        # x = self.dropout(x)
        # x = F.leaky_relu(self.bn3(self.conv3(x)), 0.33)
        # x = self.pool(x)
        # x = self.dropout(x)
        # x = F.leaky_relu(self.bn4(self.conv4(x)), 0.33)
        # g = self.pool(x)

        l = self.lstm1(y)

        g = g.flatten(start_dim=1)

        l = l[0].flatten(start_dim=1)

        x = torch.cat([g, l], dim=1)

        x = F.relu(self.fc1(x))
        self.feature = x
        x = self.fc2(x)
        # x = self.fc3(x)
        return x