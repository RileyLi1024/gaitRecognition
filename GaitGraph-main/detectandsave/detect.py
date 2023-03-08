import csv
import importlib
import itertools
from tqdm import tqdm
import decord
import os
import os.path as osp
import cv2
import moviepy.editor as mpy
import matplotlib.pyplot as plt
import numpy as np
import mmcv
from mmdet.apis import inference_detector, init_detector
from mmpose.apis import init_pose_model, inference_top_down_pose_model, vis_pose_result
from abc import abstractproperty
from tracker import *



args = abstractproperty()
args.det_config = ('faster_rcnn_r50_fpn_2x_coco.py')
args.det_checkpoint = ('faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth')
args.device = 'cuda:0'
args.pose_config = ('hrnet_w32_coco_256x192.py')
args.pose_checkpoint = ('hrnet_w32_coco_256x192-c78dce93_20200708.pth')
args.detectpath = ('multiperson.mp4')

vid = decord.VideoReader(args.detectpath)
imgs = [x.asnumpy() for x in vid]
# Perform person detection
model = init_detector(args.det_config, args.det_checkpoint, args.device)
print('detect person')
results = [inference_detector(model, img) for img in tqdm(imgs)]
print('detect person finish')
# Threshold with bbox score 0.8
print('choose person config>0.8')
results = [result[0][result[0][:, 4] >= 0.8] for result in tqdm(results)]
print('choose person config>0.8 finish')
imgsnew = []
boxes = []
print('detect person number')
for i,result in tqdm(enumerate(results)):
    if len(result) == 0:
        boxes.append(result)
        imgsnew.append(imgs[i])
        continue
    img,box = update_tracker(result, imgs[i])
    imgsnew.append(img)
    boxes.append(box)
print('detect person number finish')
#
# for i in imgsnew:
#     cv2.imshow('img', i)
#     cv2.waitKey(10)
# cv2.destroyAllWindows()

modelpose = init_pose_model(args.pose_config, args.pose_checkpoint, args.device)
print('detect person pose')
poses = [
    inference_top_down_pose_model(modelpose,
                                  img,
                                  [dict(bbox=x) for x in list(result)],
                                  format='xyxy')[0]
    for img, result in tqdm(zip(imgs, results))
]
print('detect person pose finish')

print('range person')
person = []
for i, box in enumerate(boxes):
    if len(box) == 0:
        continue
    for j, b in enumerate(box):
        person.append(b[4])
person = set(person)
print('range person finish')
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
## 2D
file = open('TOTAL.csv', "w", newline='')
writer = csv.writer(file)
header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
writer.writerow(["image_name"] + list(itertools.chain.from_iterable(header)))
print('save pose')
for n,p in tqdm(enumerate(person)):
    name='./'+str(n+1).zfill(3)+'-nm-01-000'+'/000001.jpg'
    for i,box in enumerate(boxes):
        if len(box)==0:
            continue
        for j,b in enumerate(box):
            if b[4]==p:
                try:
                    pose = poses[i][j]['keypoints']
                except: continue
                writer.writerow([name] + list(pose.reshape(-1)))
print('save pose finsih')
print('save mp4')
img2video(imgsnew)
print('save mp4 finish')