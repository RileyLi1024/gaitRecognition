import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms

x = 1


class Cnn(nn.Module):
    # 一般在__init__中定义网络需要的操作算子，比如卷积、全连接算子等等
    def __init__(self):
        super(CnnLstm, self).__init__()
        # Conv2d的第一个参数是输入的channel数量，第二个是输出的channel数量，第三个是kernel size,第四个是步长的大小

        self.conv1 = nn.Conv2d(1, 32, 2, 1, padding=1)
        self.conv2 = nn.Conv2d(32, 32, 2, 1, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 2, 1, padding=1)
        self.conv4 = nn.Conv2d(64, 64, 2, 1, padding=1)
        self.conv5 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv6 = nn.Conv2d(128, 128, 2, 1, padding=1)
        self.conv7 = nn.Conv2d(128, 256, 2, 1, padding=1)
        self.conv8 = nn.Conv2d(256, 256, 2, 1, padding=1)

        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)
        self.lstm1 = nn.LSTM(51, 256)

    # forward这个函数定义了前向传播的运算，只需要像写普通的python算数运算那样就可以了
    def forward(self, x):
        x = F.leaky_relu(self.conv1(x), 0.33)
        x = self.pool(x)
        x = F.leaky_relu(self.conv2(x), 0.33)
        x = self.pool(x)
        x = F.leaky_relu(self.conv3(x), 0.33)
        x = self.pool(x)
        x = F.leaky_relu(self.conv4(x), 0.33)
        x = self.pool(x)
        x = F.leaky_relu(self.conv5(x), 0.33)
        g = self.pool(x)

        # x = F.leaky_relu(self.conv6(x), 0.33)
        # x = self.pool(x)
        # x = F.leaky_relu(self.conv7(x), 0.33)
        # x = self.pool(x)
        # x = F.leaky_relu(self.conv8(x), 0.33)
        # g = self.pool(x)
        return g


class Lstm(nn.Module):
    # 一般在__init__中定义网络需要的操作算子，比如卷积、全连接算子等等
    def __init__(self):
        super(Lstm, self).__init__()

        self.lstm1 = nn.LSTM(input_size=45, hidden_size=128, batch_first=True)

    def forward(self, x):
        l = self.lstm1(x)
        return l


class Fc(nn.Module):
    def __init__(self):
        super(Fc, self).__init__()
        self.fc1 = nn.Linear(7040, 1000)
        self.fc2 = nn.Linear(1000, 50)
        self.fc3 = nn.Linear(50, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.sigmoid(self.fc3(x))

        return x


class TwoStreamNet_sianese(nn.Module):
    def __init__(self):
        super(TwoStreamNet_sianese, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 2, 1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 2, 1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv4 = nn.Conv2d(128, 256, 2, 1, padding=1)

        self.conv5 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv6 = nn.Conv2d(128, 128, 2, 1, padding=1)
        self.conv7 = nn.Conv2d(128, 256, 2, 1, padding=1)
        self.conv8 = nn.Conv2d(256, 256, 2, 1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)

        self.lstm1 = nn.LSTM(input_size=44, hidden_size=64, batch_first=True)

        self.fc1 = nn.Linear(6272, 128)  # out128
        self.fc2 = nn.Linear(128, 2)
        self.feature = []
        self.feature2 = []

    def forward(self, x1, x2, y1, y2):
        x1 = F.leaky_relu(self.conv1(x1), 0.33)
        x1 = self.pool(x1)
        x1 = self.dropout(x1)
        x1 = F.leaky_relu(self.conv2(x1), 0.33)
        x1 = self.pool(x1)
        self.feature2 = x1
        x1 = self.dropout(x1)
        x1 = F.leaky_relu(self.conv3(x1), 0.33)
        x1 = self.pool(x1)
        x1 = self.dropout(x1)
        x1 = F.leaky_relu(self.conv4(x1), 0.33)
        g1 = self.pool(x1)

        x2 = F.leaky_relu(self.conv1(x2), 0.33)
        x2 = self.pool(x2)
        x2 = self.dropout(x2)
        x2 = F.leaky_relu(self.conv2(x2), 0.33)
        x2 = self.pool(x2)
        self.feature2 = x2
        x2 = self.dropout(x2)
        x2 = F.leaky_relu(self.conv3(x2), 0.33)
        x2 = self.pool(x2)
        x2 = self.dropout(x2)
        x2 = F.leaky_relu(self.conv4(x2), 0.33)
        g2 = self.pool(x2)

        l1 = self.lstm1(y1)
        l2 = self.lstm1(y2)

        g1 = g1.flatten(start_dim=1)
        g2 = g2.flatten(start_dim=1)

        l1 = l1[0].flatten(start_dim=1)
        l2 = l2[0].flatten(start_dim=1)

        x = torch.cat([g1, g2, l1, l2], dim=1)
        x = F.relu(self.fc1(x))
        self.feature = x
        x = self.dropout(x)
        x = self.fc2(x)
        # x = self.fc3(x)
        return x

    def get_fc2(self, x, y):
        x = F.leaky_relu(self.conv1(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv2(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv3(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv4(x), 0.33)

        g = self.pool(x)

        l = self.lstm1(y)

        # g = g.view(batch_size, -1)
        # # l = l[0].view(1, -1)
        # l = l[0].reshape(batch_size, -1)

        g = g.flatten(start_dim=1)
        l = l[0].flatten(start_dim=1)

        x = torch.cat([g, l], dim=1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)

        return x


class TwoStreamNet(nn.Module):
    def __init__(self):
        super(TwoStreamNet, self).__init__()
        self.conv1 = nn.Conv2d(2, 32, 2, 1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 2, 1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv4 = nn.Conv2d(128, 256, 2, 1, padding=1)

        self.conv5 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv6 = nn.Conv2d(128, 128, 2, 1, padding=1)
        self.conv7 = nn.Conv2d(128, 256, 2, 1, padding=1)
        self.conv8 = nn.Conv2d(256, 256, 2, 1, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)

        self.lstm1 = nn.LSTM(input_size=88, hidden_size=64, batch_first=True)

        self.fc1 = nn.Linear(6272, 128)  # out128
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
        # !!!这里有个问题，lstm如何进入多通道数据
        x = torch.cat((x1, x2), 1)   # 按通道拼接cnn1和cnn2，cnn1[b,1,50,44]+cnn2[b,1,50,44]->[b,2,50,44]
        y = torch.cat((y1, y2), 2)    # 按特征拼接lstm1和lstm2，lstm1[b,50,44]+lstm2[b,50,44]->[b,50,88]

        x = F.leaky_relu(self.conv1(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv2(x), 0.33)
        x = self.pool(x)
        self.feature2 = x
        x = self.dropout(x)
        x = F.leaky_relu(self.conv3(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv4(x), 0.33)
        g = self.pool(x)


        l = self.lstm1(y)


        g = g.flatten(start_dim=1)


        l = l[0].flatten(start_dim=1)


        x = torch.cat([g, l], dim=1)
        x = F.relu(self.fc1(x))
        self.feature = x
        x = self.dropout(x)
        x = self.fc2(x)
        # x = self.fc3(x)
        return x

    def get_fc2(self, x, y):
        x = F.leaky_relu(self.conv1(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv2(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv3(x), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.conv4(x), 0.33)

        g = self.pool(x)

        l = self.lstm1(y)

        # g = g.view(batch_size, -1)
        # # l = l[0].view(1, -1)
        # l = l[0].reshape(batch_size, -1)

        g = g.flatten(start_dim=1)
        l = l[0].flatten(start_dim=1)

        x = torch.cat([g, l], dim=1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)

        return x

class TwoStreamNet2_bn(nn.Module):
    def __init__(self):
        super(TwoStreamNet2_bn, self).__init__()
        self.conv1 = nn.Conv2d(2, 32, 2, 1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 2, 1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv4 = nn.Conv2d(128, 256, 2, 1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(64)
        self.bn3 = nn.BatchNorm2d(128)
        self.bn4 = nn.BatchNorm2d(256)

        # self.conv5 = nn.Conv2d(64, 128, 2, 1, padding=1)
        # self.conv6 = nn.Conv2d(128, 128, 2, 1, padding=1)
        # self.conv7 = nn.Conv2d(128, 256, 2, 1, padding=1)
        # self.conv8 = nn.Conv2d(256, 256, 2, 1, padding=1)

        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)

        self.lstm1 = nn.LSTM(input_size=88, hidden_size=64, batch_first=True)

        self.fc1 = nn.Linear(6272, 128)  # out128
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
        # !!!这里有个问题，lstm如何进入多通道数据
        x = torch.cat((x1, x2), 1)   # 按通道拼接cnn1和cnn2，cnn1[b,1,50,44]+cnn2[b,1,50,44]->[b,2,50,44]
        y = torch.cat((y1, y2), 2)    # 按特征拼接lstm1和lstm2，lstm1[b,50,44]+lstm2[b,50,44]->[b,50,88]

        x = F.leaky_relu(self.bn1(self.conv1(x)), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.bn2(self.conv2(x)), 0.33)
        x = self.pool(x)
        self.feature2 = x
        x = self.dropout(x)
        x = F.leaky_relu(self.bn3(self.conv3(x)), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.bn4(self.conv4(x)), 0.33)
        g = self.pool(x)


        l = self.lstm1(y)


        g = g.flatten(start_dim=1)


        l = l[0].flatten(start_dim=1)


        x = torch.cat([g, l], dim=1)
        x = F.relu(self.fc1(x))
        self.feature = x
        x = self.dropout(x)
        x = self.fc2(x)
        # x = self.fc3(x)
        return x

class TwoStreamNet2_bn(nn.Module):
    '''
    第二次数据的模型，data2相比之前的数据，每个samle少了3列
    '''
    def __init__(self):
        super(TwoStreamNet2_bn, self).__init__()
        self.conv1 = nn.Conv2d(2, 32, 2, 1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 2, 1, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 2, 1, padding=1)
        self.conv4 = nn.Conv2d(128, 256, 2, 1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(64)
        self.bn3 = nn.BatchNorm2d(128)
        self.bn4 = nn.BatchNorm2d(256)

        # self.conv5 = nn.Conv2d(64, 128, 2, 1, padding=1)
        # self.conv6 = nn.Conv2d(128, 128, 2, 1, padding=1)
        # self.conv7 = nn.Conv2d(128, 256, 2, 1, padding=1)
        # self.conv8 = nn.Conv2d(256, 256, 2, 1, padding=1)

        self.pool = nn.MaxPool2d(2, 2)
        self.dropout = nn.Dropout(0.25)

        self.lstm1 = nn.LSTM(input_size=88, hidden_size=64, batch_first=True)

        self.fc1 = nn.Linear(6272, 128)  # out128
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

        x = F.leaky_relu(self.bn1(self.conv1(x)), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.bn2(self.conv2(x)), 0.33)
        x = self.pool(x)
        self.feature2 = x
        x = self.dropout(x)
        x = F.leaky_relu(self.bn3(self.conv3(x)), 0.33)
        x = self.pool(x)
        x = self.dropout(x)
        x = F.leaky_relu(self.bn4(self.conv4(x)), 0.33)
        g = self.pool(x)


        l = self.lstm1(y)


        g = g.flatten(start_dim=1)


        l = l[0].flatten(start_dim=1)


        x = torch.cat([g, l], dim=1)
        x = F.relu(self.fc1(x))
        self.feature = x
        x = self.dropout(x)
        x = self.fc2(x)
        # x = self.fc3(x)
        return x