import pandas as pd
import os
import numpy as np

root = r'G:\Code\tf2_torch\pytorch\2_Projects\cnn+lstm\data\data1'
file_dir = os.listdir(root)
label_list=[]
i=1
for file in file_dir:
    data_df = pd.read_csv(os.path.join(root,file))
    data1_label_df = data_df.iloc[:, :1]
    data1_label = data1_label_df.iloc[0, 0]
    data1_label = np.array((data1_label[:3]), dtype=np.float64).reshape(-1)
    # data1_label = torch.from_numpy(data1_label).type(torch.FloatTensor)
    # print(file)
    # if (data1_label<1 or data1_label>60):
    #     print("erro:",file)
    if data1_label not in label_list:
        label_list.append(data1_label)
        i+=1
        print(i)