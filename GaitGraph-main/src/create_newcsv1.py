import itertools
import csv
import os
import numpy as np
from tqdm import  tqdm
from glob import glob
import pandas as pd
keypoints = {
    0: "nose",
    1: "left_eye",
    2: "right_eye",
    3: "left_ear",
    4: "right_ear",
    5: "left_shoulder",
    6: "right_shoulder",
    7: "left_elbow",
    8: "right_elbow",
    9: "left_wrist",
    10: "right_wrist",
    11: "left_hip",
    12: "right_hip",
    13: "left_knee",
    14: "right_knee",
    15: "left_ankle",
    16: "right_ankle"
}
def write_csv(filename, pose):
    file = open(filename, "w", newline='')
    writer = csv.writer(file)
    header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
    writer.writerow(["image_name"] + list(itertools.chain.from_iterable(header)))
    writer.writerow(list(pose.reshape(-1)))
    file.close()

data_list_path = './verity_detectresults_out'
csvs = sorted(glob(data_list_path+'/*/*/*.csv'))
test_name = 'test'
file_pathpose='/home/nscn/user/shy/GaitGraph-main/save'
cvs_name = file_pathpose + '/'+test_name+'.csv'
file = open(cvs_name, "w", newline='')
writer = csv.writer(file)
header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
writer.writerow(["image_name"] + list(itertools.chain.from_iterable(header)))
#./0-nm-01-000/00001.jpg
for csv in tqdm(csvs):
    data = str(np.loadtxt(csv, skiprows=1, dtype=str)).split(",")
    person = csv.split('0000')[1].split('/')[0]
    name = './'+person+'-nm-01-000/'+csv.split('/')[-1]
    writer.writerow([name] + data)
file.close()
#读取你要拼接的3个csv文件
data1=pd.read_csv(file_pathpose+'/zt.csv')  #data1为DataFrame格式
data1.to_csv(file_pathpose+'/test.csv',index=False,header=False,mode='a+')