import os

from mmdet.apis import inference_detector, init_detector
from mmpose.apis import init_pose_model, inference_top_down_pose_model, vis_pose_result
from abc import abstractproperty
from tracker import *
from glob import glob
import csv
import importlib
import itertools
import os.path as osp
import decord
def plot_bboxes(image, bboxes, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    for (x1, y1, x2, y2, pos_id) in bboxes:
        cls_id=''
        color = (0, 255, 0)
        c1, c2 = (x1, y1), (x2, y2)
        cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(image, '{} ID-{}'.format(cls_id, pos_id), (c1[0], c1[1] - 2), 0, tl / 3,
                    [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    return image

def write_csv(filename, pose):
    file = open(filename, "w", newline='')
    writer = csv.writer(file)
    header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
    writer.writerow(list(itertools.chain.from_iterable(header)))
    writer.writerow(list(pose.reshape(-1)))
    file.close()

args = abstractproperty()
args.det_config = ('faster_rcnn_r50_fpn_2x_coco.py')
args.det_checkpoint = ('faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth')
args.device = 'cuda:0'
args.pose_config = ('hrnet_w32_coco_256x192.py')
args.pose_checkpoint = ('hrnet_w32_coco_256x192-c78dce93_20200708.pth')
model = init_detector(args.det_config, args.det_checkpoint, args.device)
modelpose = init_pose_model(args.pose_config, args.pose_checkpoint, args.device)
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
box_results = []
img_results = []
id_results = []
vid = decord.VideoReader('test.mp4')
imgs = [x.asnumpy() for x in vid]
out_path = "./yanzheng_detectresults_out"

for i,image in tqdm(enumerate(imgs),total=len(imgs)):

    results_ptp = inference_detector(model, image)
    results_ptp = results_ptp[0][results_ptp[0][:, 4] >= 0.8]
    box_results.append(results_ptp)
    if len(results_ptp)==0:
        # img_results.append(image)
        # id_results.append([])
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
    for a,value in enumerate(list(outputs)):
        pose =  hrent_pose[a]['keypoints']
        scores = pose[:,2]
        if min(scores) < 0.2:
            continue
        x1, y1, x2, y2, track_id = value
        id_results.append(track_id)
        file_pathpose = out_path + '/person' + str(track_id).zfill(4) + '/HRnet_pose'
        file_pathimg = out_path + '/person' + str(track_id).zfill(4) + '/img'
        os.makedirs(file_pathpose, exist_ok=True)
        os.makedirs(file_pathimg, exist_ok=True)
        num = id_results.count(track_id)
        cvs_name = file_pathpose + '/' + str(num).zfill(3) + '.csv'
        img_name = file_pathimg + '/' + str(num).zfill(3) + '.png'
        img = image[y1:y2, x1:x2, :]
        imageio.imwrite(img_name,img)
        write_csv(cvs_name, pose)




