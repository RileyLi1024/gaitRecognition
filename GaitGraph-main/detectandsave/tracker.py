import csv
import itertools
import os
import numpy as np
from mmdet.apis import inference_detector
from tqdm import tqdm
import imageio
from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort
import torch
import cv2

palette = (2 ** 11 - 1, 2 ** 15 - 1, 2 ** 20 - 1)
cfg = get_config()
cfg.merge_from_file("E:/workspace-sts/Gait/GaitGraph-main/detectandsave/deep_sort/configs/deep_sort.yaml")
deepsort = DeepSort(cfg.DEEPSORT.REID_CKPT,
                    max_dist=cfg.DEEPSORT.MAX_DIST, min_confidence=cfg.DEEPSORT.MIN_CONFIDENCE,
                    nms_max_overlap=cfg.DEEPSORT.NMS_MAX_OVERLAP, max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                    max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                    use_cuda=True)


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

def plot_bboxes(img, bboxes, line_thickness=None):
    # Plots one bounding box on image img
    image = img.copy()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    for (x1, y1, x2, y2, pos_id) in bboxes:
        cls_id=''
        color = (0, 255, 0)
        c1, c2 = (x1, y1), (x2, y2)
        cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(cls_id, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0], c1[1]
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(image, 'ID-{}'.format(pos_id), (c1[0], c1[1] - 2), 0, tl / 3,
                    [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    return image


def update_tracker(results, image):

        bbox_xywh = []
        confs = []
        bboxes2draw = []
        for bbox in results:
            # Adapt detections to deep sort input format
            x1, y1, x2, y2, conf = bbox[0], bbox[1], bbox[2], bbox[3], bbox[4]
            obj = [(x1 + x2) / 2, (y1 + y2) / 2, x2 - x1, y2 - y1]
            bbox_xywh.append(obj)
            confs.append(conf)
        xywhs = torch.Tensor(bbox_xywh)
        confss = torch.Tensor(confs)
        # Pass detections to deepsort
        # outputs = deepsort.update(xywhs, confss, image)
        for i in range(3):
            outputs = deepsort.update(xywhs, confss, image)
        for value in list(outputs):
            x1, y1, x2, y2, track_id = value
            bboxes2draw.append(
                (x1, y1, x2, y2,track_id)
            )
        image1 = plot_bboxes(image, bboxes2draw)

        return image1, bboxes2draw

def update_trackerptp(model, image):
    bbox_xywh = []
    confs = []
    bboxes2draw = []
    image = np.asarray(imageio.imread(image))
    results_ptp = inference_detector(model, image)
    results_ptp = results_ptp[0][results_ptp[0][:, 4] >= 0.8]
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
    for value in list(outputs):
        x1, y1, x2, y2, track_id = value
        bboxes2draw.append(
            (x1, y1, x2, y2, track_id)
        )
    image_ptp = plot_bboxes(image, bboxes2draw)
    return results_ptp , image_ptp, bboxes2draw

def img2video(videopath,videoname):
    imgs = os.listdir(videopath)
    fps = 20
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    img = imgs[0]
    size = (img.shape[1], img.shape[0])
    videoWrite = cv2.VideoWriter(videoname, fourcc, fps, size)

    for name in tqdm(imgs):
        videoWrite.write(name)
    videoWrite.release()

def write_csv(filename, pose):
    file = open(filename, "w", newline='')
    writer = csv.writer(file)
    header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
    writer.writerow(list(itertools.chain.from_iterable(header)))
    writer.writerow(list(pose.reshape(-1)))
    file.close()