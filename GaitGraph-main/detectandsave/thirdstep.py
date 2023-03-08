import os

import decord
from mmdet.apis import inference_detector, init_detector
from mmpose.apis import init_pose_model, inference_top_down_pose_model, vis_pose_result
from abc import abstractproperty
from tracker import *
from glob import glob
import csv
import importlib
import itertools
import os.path as osp
args = abstractproperty()
args.det_config = ('faster_rcnn_r50_fpn_2x_coco.py')
args.det_checkpoint = ('faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth')
args.device = 'cuda:0'
args.pose_config = ('hrnet_w32_coco_256x192.py')
args.pose_checkpoint = ('hrnet_w32_coco_256x192-c78dce93_20200708.pth')

args.inputvideo = ("E:/user/shy/GaitGraph-main/detectandsave/二楼东门厅进口_3min20-3min45.mp4")    # 第三步就是输入判断的视频
vid = decord.VideoReader(args.inputvideo)
frames = [x.asnumpy() for x in vid]
out_path = "./verity_detectresults_out" + args.inputvideo.split('/')[-1]
model = init_detector(args.det_config, args.det_checkpoint, args.device)
modelpose = init_pose_model(args.pose_config, args.pose_checkpoint, args.device)

img_results = []
id_results = []
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = 30
img = frames[0]
size = (img.shape[1], img.shape[0])
videoWrite = cv2.VideoWriter('./video/verity'+args.inputvideo.split('/')[-1], fourcc, fps, size)
for i,image in tqdm(enumerate(frames),total=len(frames)):
    results_ptp = inference_detector(model, image)
    results_ptp = results_ptp[0][results_ptp[0][:, 4] >= 0.8]

    if len(results_ptp)==0:
        continue
    hrent_pose=inference_top_down_pose_model(modelpose, image, [dict(bbox=x) for x in list(results_ptp)],
                                  format='xyxy')[0]
    bbox_xywh = []
    confs = []
    bboxes2draw = []
    for bbox in results_ptp:
        # Adapt detections to deep sort input format
        x1, y1, x2, y2, conf = bbox[0], bbox[1], bbox[2], bbox[3], bbox[4]
        obj = [(x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1]
        bbox_xywh.append(obj)
        confs.append(conf)
    xywhs = torch.Tensor(bbox_xywh)
    confss = torch.Tensor(confs)
    # Pass detections to deepsort
    for i in range(3):
        outputs = deepsort.update(xywhs, confss, image)
    bboxes2draw = []
    for a,value in enumerate(list(outputs)):
        pose =  hrent_pose[a]['keypoints']
        scores = pose[:,2]
        if min(scores) < 0.2:
            continue
        x1, y1, x2, y2, track_id = value
        id_results.append(track_id)
        file_pathpose = out_path + '/' + str(track_id).zfill(3) + '/HRnet_pose'
        file_pathimg = out_path + '/' + str(track_id).zfill(3) + '/img'
        os.makedirs(file_pathpose, exist_ok=True)
        os.makedirs(file_pathimg, exist_ok=True)
        num = id_results.count(track_id)
        cvs_name = file_pathpose + '/' + str(num).zfill(3) + '.csv'
        img_name = file_pathimg + '/' + str(num).zfill(3) + '.png'
        img = image[y1:y2, x1:x2, :]
        imageio.imwrite(img_name,img)
        write_csv(cvs_name, pose)
        bboxes2draw.append(
            (x1, y1, x2, y2, track_id)
        )
    img = plot_bboxes(image, bboxes2draw)
    videoWrite.write(img)
videoWrite.release()




