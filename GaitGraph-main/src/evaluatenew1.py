import os
import sys
import time
from glob import glob

import cv2
import imageio
from tqdm import tqdm

sys.path.append(r'E:/workspace-sts/Gait/GaitGraph-main/src')

import numpy as np
import os.path as osp
import torch
from torchvision import transforms
from torch.utils.data import DataLoader
import json
from common import get_model_resgcn
from utils import AverageMeter
from datasets import dataset_factory
from datasets.augmentation import ShuffleSequence, SelectSequenceCenter, ToTensor, MultiInput
from datasets.graph import Graph
from collections import Counter
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



def create_csv(verity_path,out_path ,test_path):
    """
    #第一个参数是需要追踪视频的路径，第二个参数是最后保存csv文件的地址，第三个参数是待判别人的地址
    """
    import csv
    csvs = sorted(glob(verity_path + '/*/*/*.csv'))
    cvs_name = out_path + '/verity.csv'
    file = open(cvs_name, "w", newline='')
    writer = csv.writer(file)
    header = [[f"{k}_x", f"{k}_y", f"{k}_z"] for k in keypoints.values()]
    writer.writerow(["image_name"] + list(itertools.chain.from_iterable(header)))
    # ./0-nm-01-000/00001.jpg
    for csv in csvs:
        data = str(np.loadtxt(csv, skiprows=1, dtype=str)).split(",")
        person = csv.split('HRnet_pose')[0].split('\\')[1]
        name = './' + person + '-nm-01-000/' + csv.split('\\')[-1]
        writer.writerow([name] + data)
    file.close()
    test_csv = sorted(glob(test_path + '/*.csv'))
    data1 = pd.read_csv(test_csv[0])
    data1.to_csv(cvs_name, index=False, header=False, mode='a+')

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate model on dataset")
    parser.add_argument("--dataset", default="casia-b", choices=["casia-b"])
    parser.add_argument("--weights_path", default="E:/workspace-sts/Gait/GaitGraph-main/save/"
                                                  "gaitgraph_resgcn-n39-r8_coco_seq_60.pth")

    parser.add_argument("--data_path", default="E:/workspace-sts/Gait/WebContent/Graph/result_all/verity.csv")     #一个人
      #另外一个人
    parser.add_argument("--network_name", default="resgcn-n39-r8")
    parser.add_argument("--sequence_length", type=int, default=60)
    parser.add_argument("--batch_size", type=int, default=256)
    parser.add_argument("--embedding_layer_size", type=int, default=128)
    parser.add_argument("--use_multi_branch", action="store_true")
    parser.add_argument("--shuffle", action="store_true")
    parser.add_argument("--ProcessPath", default="E:/workspace-sts/Gait/WebContent/Graph/Process/",
                        help="选择追踪行人的文件处理路径")
    parser.add_argument("--ProcessVideoPath", default="E:/workspace-sts/Gait/WebContent/Graph/video_name.txt",
                        help="追踪行人视频的名字")
    parser.add_argument("--RegisterPath", default="E:/workspace-sts/Gait/WebContent/Graph/Register",
                        help="选择追踪行人的文件处理路径")
    parser.add_argument("--RegisterVideoPath", default="E:/workspace-sts/Gait/WebContent/Graph/track_person.txt",
                        help="追踪行人视频的名字")
    parser.add_argument("--data_OutPath", default="E:/workspace-sts/Gait/WebContent/Graph/result_all/")

    opt = parser.parse_args()
    file_p = open(opt.ProcessVideoPath)    #Process video name
    file_pdata = file_p.readlines()
    inputverity = file_pdata[0].split('.')[0]  # 需要传进追踪视频的参数，一个视频名
    verity_path = osp.join(opt.ProcessPath,inputverity)
    file_r = open(opt.RegisterVideoPath)  # Process video name
    file_rdata = file_r.readlines()
    inputregister = file_rdata[0]  # 需要传进待判别的参数，一个视频名+id
    test_path = opt.RegisterPath+'/'+inputregister
    test_videopath = sorted(glob(test_path + '/*.mp4'))[0]

    create_csv(verity_path, opt.data_OutPath, test_path)

    # Config for dataset
    graph = Graph("coco")
    dataset_class = dataset_factory(opt.dataset)
    evaluation_fn = None
    if opt.dataset == "casia-b":
        evaluation_fn = _evaluate_casia_b

    # Load data
    dataset = dataset_class(
        opt.data_path,
        train=False,
        sequence_length=opt.sequence_length,
        transform=transforms.Compose(
            [
                SelectSequenceCenter(opt.sequence_length),     # 选取60帧，起始位置为data.shape[0]/2-30
                ShuffleSequence(opt.shuffle),                  # 随机打乱 60*17*3
                MultiInput(graph.connect_joint, opt.use_multi_branch),
                ToTensor()
            ]
        ),
    )


    data_loader = DataLoader(dataset, batch_size=opt.batch_size)

    # Init model
    model, model_args = get_model_resgcn(graph, opt)

    if torch.cuda.is_available():
        model.cuda()

    # Load weights
    checkpoint = torch.load(opt.weights_path)
    model.load_state_dict(checkpoint["model"])
    ids = []
    for i in range(100):
        id = evaluate(data_loader, model, evaluation_fn, use_flip=True )
        ids.append(id)
    ids = list(np.array(ids).reshape(-1))
    collection_words = Counter(ids)
    # print(collection_words)
    most_counterNum = collection_words.most_common(6)
    ids = [i[0] for i in most_counterNum]
    # print("可能的预测身份")
    # print("身份：person", ids)
    video,person = inputregister.split('/')
    outpath = opt.data_OutPath+ video+person+'_'+inputverity+'/'
    os.makedirs(outpath, exist_ok=True)
    print(test_videopath.split("Register/")[1])
    for id in ids:
        inputimgs = osp.join(verity_path , str(id).zfill(3))
        outpath1= outpath + str(id).zfill(3)
        imgtovideo(inputimgs, outpath1)
        print((outpath1 + '.mp4').split("result_all/")[1])

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

def evaluate(data_loader, model, evaluation_fn, log_interval=10, use_flip=False):
    model.eval()
    batch_time = AverageMeter()

    # Calculate embeddings
    with torch.no_grad():
        end = time.time()
        embeddings = dict()
        for idx, (points, target) in enumerate(data_loader):

            if use_flip:
                bsz = points.shape[0]   #2
                data_flipped = torch.flip(points, dims=[1])     #反转
                points = torch.cat([points, data_flipped], dim=0)

            if torch.cuda.is_available():
                points = points.cuda(non_blocking=True)

            output = model(points)

            if use_flip:
                f1, f2 = torch.split(output, [bsz, bsz], dim=0)
                output = torch.mean(torch.stack([f1, f2]), dim=0)

            for i in range(output.shape[0]):
                sequence = tuple(
                    int(t[i]) if type(t[i]) is torch.Tensor else t[i] for t in target
                )
                embeddings[sequence] = output[i].cpu().numpy()

            batch_time.update(time.time() - end)
            end = time.time()
            # if idx % log_interval == 0:
            #     print(
            #         f"Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t"
            #     )
            #     sys.stdout.flush()

    return evaluation_fn(embeddings)

def _evaluate_casia_b(embeddings):
    k = list()
    v = list()
    for (i, j) in embeddings.items():
        k.append(i), v.append(j)
    c_v = v[-1].reshape(1,-1)                #将待测试的人保存在列表最后
    v.pop()
    v = np.array(v)
    distance = list(np.linalg.norm(v-c_v, ord=2, axis=1))
    # min_pos = np.argmin(distance)
    min_pos = sorted(distance)[:5]
    id = []
    for i in range(5):
        index_ = distance.index(min_pos[i])
        id.append(k[index_][0])

    return id

def sim_c(v1, v2):
    vector_a = np.mat(v1)
    vector_b = np.mat(v2)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    sim = num / denom
    return sim

if __name__ == "__main__":

    main()
