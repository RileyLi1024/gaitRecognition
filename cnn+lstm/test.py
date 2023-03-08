import torch
from torch.utils.data import DataLoader
from net.cnn_lstm import CnnLstm
from _utils.dataloader import GaitDataset


torch.cuda.manual_seed_all(1)
root_dir1 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data1_test'
root_dir2 = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data2_test'
device = torch.device('cuda')

train_dataset = GaitDataset(root_dir1, root_dir2)

# data1,data2,label1,label2 = train_dataset[1]

# out = model(data2,data1)

gen = DataLoader(train_dataset, batch_size=256, num_workers=int(0), pin_memory=True,
                 drop_last=True)


net = CnnLstm()
net.load_state_dict(torch.load(r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\logs\98_0.2880191206932068.pkl'))
net.to(device)
net.eval()

correct = 0
total = 0
count = 0
with torch.no_grad():
    for data in gen:
        data1, data2, label1, label2 = data[0], data[1], data[2], data[3]
        # forward
        data1 = data1.to(device)
        data2 = data2.to(device)
        label1 = label1.to(device, dtype=torch.int64)
        out = net(data2, data1)
        _, pred = torch.max(out, 1)
        pred_reshape = pred.reshape(-1, 1)
        a = (pred == label1)
        correct += (pred_reshape == label1).sum().item()
        total += label1.size(0)
        print('batch:{}'.format(count + 1))
        count += 1

#
# Acc
accuracy = float(correct) / total
print('Acc = {:.5f}'.format(accuracy))
