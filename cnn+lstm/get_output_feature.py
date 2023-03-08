import torch
from torch.utils.data import DataLoader
from net.cnn_lstm import CnnLstm
from _utils.dataloader import GaitDataset
import numpy as np
import matplotlib.pyplot as plt

torch.cuda.manual_seed_all(1)
root_dir1 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data1_after60'
root_dir2 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data2_after60'
device = torch.device('cuda')

train_dataset = GaitDataset(root_dir1, root_dir2)

# data1,data2,label1,label2 = train_dataset[1]

# out = model(data2,data1)

gen = DataLoader(train_dataset, batch_size=1, num_workers=int(0), pin_memory=True,
                 drop_last=True)

net = CnnLstm()
net.load_state_dict(torch.load(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\logs\98_0.2880191206932068.pkl'))
net.to(device)
net.eval()

with torch.no_grad():
    for i_num, data in enumerate(gen):
        i_num += 4846
        data1, data2, label1, label2 = data[0], data[1], data[2], data[3]
        # forward
        data1 = data1.to(device)
        data2 = data2.to(device)
        label1 = label1.to(device, dtype=torch.int64)
        # out = net.get_fc2(data2, data1).cpu().data.numpy()

        out = net(data2, data1)

        feature = net.feature.cpu().data.numpy()


        # 一段可视化卷积层的代码
        # feature_map = np.squeeze(feature, axis=0)
        # for i in range(feature_map.shape[0]):
        #
        #     plt.imshow(feature_map[i])
        #     plt.show()
        # plt.show()


        np.savetxt(r"D:/PYproject/cnn+lstm/Feature/{}.csv".format(i_num), feature,
                   delimiter=',', fmt='%.18f')
        print(feature)
