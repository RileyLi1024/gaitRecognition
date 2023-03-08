import sys
import time
sys.path.append(r'D:/QYJ_1/GaitGraph-main/src/')

import numpy as np

import torch
from torchvision import transforms
from torch.utils.data import DataLoader
import json
from common import get_model_resgcn
from utils import AverageMeter
from datasets import dataset_factory
from datasets.augmentation import ShuffleSequence, SelectSequenceCenter, ToTensor, MultiInput
from datasets.graph import Graph

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate model on dataset")
    parser.add_argument("--dataset", default="casia-b", choices=["casia-b"])
    parser.add_argument("--weights_path", default="D:/QYJ_1/GaitGraph-main/save/casia-b_models/"
                                                  "2022-03-25-16-49-40_casia-b_resgcn-n39-r8_lr_0.001_decay_1e-05_bsz_128"
                                                  "/ckpt_epoch_best.pth")
    parser.add_argument("--data_path", default="E:/workspace-sts/Gait/Matrix/GaitGraph/person1.csv")     #一个人
    parser.add_argument("--data_path1", default="E:/workspace-sts/Gait/Matrix/GaitGraph/person2.csv")    #另外一个人
    parser.add_argument("--network_name", default="resgcn-n39-r8")
    parser.add_argument("--sequence_length", type=int, default=60)
    parser.add_argument("--batch_size", type=int, default=256)
    parser.add_argument("--embedding_layer_size", type=int, default=128)
    parser.add_argument("--use_multi_branch", action="store_true")
    parser.add_argument("--shuffle", action="store_true")


    opt = parser.parse_args()

    # Config for dataset
    graph = Graph("qyj")
    dataset_class = dataset_factory(opt.dataset)

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

    dataset1 = dataset_class(
        opt.data_path1,
        train=False,
        sequence_length=opt.sequence_length,
        transform=transforms.Compose(
            [
                SelectSequenceCenter(opt.sequence_length),  # 选取60帧，起始位置为data.shape[0]/2-30
                ShuffleSequence(opt.shuffle),  # 随机打乱 60*17*3
                MultiInput(graph.connect_joint, opt.use_multi_branch),
                ToTensor()
            ]
        ),
    )

    data_loader = DataLoader(dataset, batch_size=opt.batch_size)
    data_loader1 = DataLoader(dataset1, batch_size=opt.batch_size)

    # Init model
    model, model_args = get_model_resgcn(graph, opt)

    if torch.cuda.is_available():
        model.cuda()

    # Load weights
    checkpoint = torch.load(opt.weights_path)
    model.load_state_dict(checkpoint["model"])

    feature1 = evaluate(data_loader, model, use_flip=True )
    feature2 = evaluate(data_loader1, model, use_flip=True)
    sim = sim_c(feature1, feature2)

 #   print("{:.2f}".format(sim * 100), "%")
    print("{:.2f}".format(sim))
    # print("身份：", id, walking_status[seq_type], "{:.2f}".format(sim*100), "%")



def evaluate(data_loader, model, log_interval=10, use_flip=False):
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
            k = list()
            feature = list()
            for (i, j) in embeddings.items():
                k.append(i), feature.append(j)
            #
            # batch_time.update(time.time() - end)
            # end = time.time()
            # if idx % log_interval == 0:
            #     print(
            #         f"Test: [{idx}/{len(data_loader)}]\t"
            #         f"Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t"
            #     )
            #     sys.stdout.flush()

    return feature


def sim_c(v1, v2):
    vector_a = np.mat(v1)
    vector_b = np.mat(v2)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    sim = num / denom
    return sim

if __name__ == "__main__":
    main()
