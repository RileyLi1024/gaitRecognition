"""
第二步就是选择待检测行人，生成其关节文件以及一段行人行走视频
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
import os.path as osp
import sys
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
    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    img = np.asarray(imageio.imread(imgs[0]))
    size = (img.shape[1], img.shape[0])
    videoWrite = cv2.VideoWriter(outpath+ '.mp4', fourcc, fps, size)
    for img in imgs:
        img = np.asarray(imageio.imread(img))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, size)
        videoWrite.write(img)
    videoWrite.release()


def create_csv(input_path,out_path):
    import csv
    csvs = sorted(glob(input_path + '/*/*.csv'))
    cvs_name = out_path + '.csv'
    file = open(cvs_name, "w", newline='')
    writer = csv.writer(file)
    header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
    writer.writerow(["image_name"] + list(itertools.chain.from_iterable(header)))
    # ./0-nm-01-000/00001.jpg
    for csv in csvs:
        data = str(np.loadtxt(csv, skiprows=1, dtype=str)).split(",")
        if min(data) < '0.5':
            continue
        name = './999-nm-01-000/' + csv.split('\\')[-1]
        writer.writerow([name] + data)
    file.close()

if __name__ == '__main__':

    args = abstractproperty()
    id = sys.argv[1]
    args.chooseperson = (id)  # 第二步输入嫌疑人的id,生成嫌疑人的csv文件以及视频文件
    file = open("E:/workspace-sts/Gait/WebContent/Graph/video_name.txt")
    file_data = file.readlines()
    args.inputvideo = file_data[0] # 这是第一步的输入的嫌疑人视频
    input_path = "E:/workspace-sts/Gait/WebContent/Graph/Process/" + args.inputvideo.split('.')[0]+'/'
    input_path = osp.join(input_path, args.chooseperson)
    out_path = "E:/workspace-sts/Gait/WebContent/Graph/Register/"+args.inputvideo.split('.')[0]+'/'+args.chooseperson+'/'
    os.makedirs(out_path, exist_ok=True)
    out_path = out_path + args.chooseperson
    imgtovideo(input_path, out_path)
    create_csv(input_path, out_path)

