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


class CnnLstm(nn.Module):
    def __init__(self):
        super(CnnLstm, self).__init__()
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

        self.fc1 = nn.Linear(6272, 128)#out128
        self.fc2 = nn.Linear(128, 61)
        self.feature = []
        self.feature2 = []

    def forward(self, x, y):
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
        x =self.fc2(x)
        # x = self.fc3(x)
        return x

    def get_fc2(self,x,y):
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