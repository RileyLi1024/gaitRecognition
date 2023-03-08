#!/bin/bash
# Download weights for vanilla YOLOv3
curl -O https://pjreddie.com/media/files/yolov3.weights --header "Referer: pjreddie.com"
# Download weights for tiny YOLOv3
curl -O https://pjreddie.com/media/files/yolov3-tiny.weights --header "Referer: pjreddie.com"
## Download weights for backbone network
#curl -O https://pjreddie.com/media/files/darknet53.conv.74 --header "Referer: pjreddie.com"

# Download pre-trained weights
curl -LJO https://github.com/tteepe/GaitGraph/releases/download/v0.1/gaitgraph_resgcn-n39-r8_coco_seq_60.pth

echo "#############################################################"
echo "######## Weights for HRNet Pose Estimation need to ##########"
echo "######## be downloaded manually from here:         ##########"
echo "######## https://drive.google.com/drive/folders/1nzM_OBV9LbAEA7HClC0chEyf_7ECDXYA"
echo "######## Files: pose_hrnet_*.pth                   ##########"
echo "#############################################################"
