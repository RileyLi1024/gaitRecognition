import os
from multiprocessing import Pool
from mmdet.apis import inference_detector, init_detector
from mmpose.apis import init_pose_model, inference_top_down_pose_model, vis_pose_result
from abc import abstractproperty
from tracker import *
from glob import glob
import csv
import importlib
import itertools
import os.path as osp
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





if __name__ == "__main__":
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    frames = sorted(glob("/home/nscn/datasets/iLIDS-VID/*/*/*/*/*.png"))
    # model = init_detector(args.det_config, args.det_checkpoint, args.device)
    modelpose = init_pose_model(args.pose_config, args.pose_checkpoint, args.device)
    pool = Pool(8)

    for i,image in tqdm(enumerate(frames),total=len(frames)):
        a = image.split('/')
        file_pathpose = osp.join('/', a[1], a[2], a[3], a[4], a[5], a[6] + '_2dpose', a[7],a[8])
        image = np.asarray(imageio.imread(image))
        # results_ptp = inference_detector(model, image)
        results_ptp = np.array([[0,0,64,128,1]])
        # box_results.append(results_ptp)
        hrent_pose = inference_top_down_pose_model(modelpose, image, [dict(bbox=x) for x in list(results_ptp)],
                                                   format='xyxy')[0]
        pose = hrent_pose[0]['keypoints']
        scores = pose[:, 2]
        os.makedirs(file_pathpose, exist_ok=True)
        cvs_name = file_pathpose + '/' + a[9].split('.')[0] + '.csv'
        write_csv(cvs_name, pose)


