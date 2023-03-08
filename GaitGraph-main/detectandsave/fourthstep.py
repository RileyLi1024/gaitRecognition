"""
第四步步就是根据待检测行人，从另一段视频中找到这个人，显示ID以及视频
"""
import itertools
import os
from glob import glob

import decord
import imageio
import numpy as np
import cv2
import csv
from abc import abstractproperty

import pandas as pd
from tqdm import tqdm
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

def imgtovideo(inputimgs, outpath):
    imgs = sorted(glob(inputimgs+'/*/*.png'))
    fps = 20
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    img = np.asarray(imageio.imread(imgs[0]))
    size = (img.shape[1], img.shape[0])
    videoWrite = cv2.VideoWriter(outpath+ '.mp4', fourcc, fps, size)
    for img in imgs:
        img = np.asarray(cv2.imread(img))
        img = cv2.resize(img, size)
        videoWrite.write(img)
    videoWrite.release()


def create_csv(verity_path,out_path ,test_path):
    import csv
    csvs = sorted(glob(verity_path + '/*/*/*.csv'))
    cvs_name = out_path + '/verity.csv'
    file = open(cvs_name, "w", newline='')
    writer = csv.writer(file)
    header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
    writer.writerow(["image_name"] + list(itertools.chain.from_iterable(header)))
    # ./0-nm-01-000/00001.jpg
    for csv in tqdm(csvs):
        data = str(np.loadtxt(csv, skiprows=1, dtype=str)).split(",")
        person = csv.split('out')[1].split('\\')[1]
        name = './' + person + '-nm-01-000/' + csv.split('\\')[-1]
        writer.writerow([name] + data)
    file.close()
    # 读取你要拼接的3个csv文件
    data1 = pd.read_csv(test_path)
    data1.to_csv(cvs_name, index=False, header=False, mode='a+')


if __name__ == '__main__':
    args = abstractproperty()
    args.chooseperson = ('008')   #第二步输入参数
    # os.makedirs(out_path, exist_ok=True)
    verity_path = './verity_detectresults_out二楼东门厅进口_3min20-3min45.mp4'
    out_path = './verity'
    os.makedirs(out_path, exist_ok=True)
    test_path = "./susbpect/" + args.chooseperson+'.csv'
    create_csv(verity_path,out_path ,test_path)
