# -*- coding: utf-8 -*-
# @Time    : 2022/1/1 20:14
# @Author  : Rey
# @FileName: video_demo.py
# @Software: PyCharm


import argparse
import os
import sys
import shutil
import cv2

sys.path.append("3d-pose/src")
from openpose_3dpose_sandbox import twoDcoordsToThreeDcoords


import openpyxl
import pandas as pd
import time
import subprocess



#if len(sys.argv) < 3:
    #print("print type command line parameters...")
'''
parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="input directory")
parser.add_argument("type", type=str, help="i(image) or v(video)")
args = parser.parse_args()
'''
#videoPath = './input/video/001-bg-01-000.avi'
#videoPath = './input/video/person03_walking_d2_uncomp.avi'

def main():
    #imagePath = ''
    #videoPath = './input/video/001-bg-01-000.avi'


    #videoPath = args.path
    #if os.path.exists(videoPath) is not True:
        #return
    cvtImageOutPath = "./temp/image/"

    def extracteFrames(videoPath, outputPath):
        vidCap = cv2.VideoCapture(videoPath)
        count = 0
        success = True
        while success:
            success, image = vidCap.read()
            if success is not True:
                break
            cv2.imwrite(outputPath + "frame%d.png" % count, image)
            count += 1

    if os.path.exists(cvtImageOutPath) is True:
        shutil.rmtree(cvtImageOutPath)
    os.makedirs(cvtImageOutPath)
    print("start extract frames from video...")
    extracteFrames(videoPath, cvtImageOutPath)
    print("frame extraction completed.")
    if os.path.exists(cvtImageOutPath + "../2dPose") is True:
        shutil.rmtree(cvtImageOutPath + "../2dPose")
        os.makedirs(cvtImageOutPath + "../2dPose")
    orignalPath = os.getcwd()
    print(orignalPath)
    os.chdir("E:/0_Code/0_MyCode/Action_recognition/3DPose-keypoints/openpose/")

    openPoseCmd = "bin/OpenPoseDemo.exe --image_dir " + \
                      "../" + cvtImageOutPath + " --write_json " + "../" \
                      + cvtImageOutPath + "../2dPose"

    openPoseCmd = openPoseCmd.replace('/', "\\")
    os.system(openPoseCmd)

    os.chdir(orignalPath)
    os.chdir("E:/0_Code/0_MyCode/Action_recognition/3DPose-keypoints/3d-pose")
    outputPath = "../output/"

    if os.path.exists(outputPath) is True:
        shutil.rmtree(outputPath)
    os.makedirs(outputPath)




    twoDcoordsToThreeDcoords("../" + cvtImageOutPath + "../2dPose",outputPath)

    #twoDcoordsToThreeDcoords("." + cvtImageOutPath + "../2dPose", outputPath)

    return
    #exit()



if __name__ == "__main__":

    Path = './input/Coffee_room_01/'



    i = 22
    #从  21  开始提取




    video_list = os.listdir(Path)
    video_num = len(video_list)
    print(video_num)

    n = i
    i = i - 1

    video_name = str(video_list[i])
    #video_name = video_name[1: 3]
    videoPath = Path + video_name

    main()

    file_list = os.listdir('../output/')
    file_num = len(file_list)
    print(file_num)

    w = openpyxl.Workbook()
    sheet1 = w.create_sheet('Sheet1', index=0)

    # 整合每帧关节点数据到一个文件里
    for j in range(file_num):
        file_name = str(file_list[j])
        #file_name = file_name[1: 3]
        # lable = [int(file_name) - 1]
        #lable = [int(8)]
        # print(lable)

        # 读取数据
        datapath = '../output/' + file_list[j]
        f = open(datapath)
        d = pd.read_csv(f, header=None, encoding="utf_8_sig")
        # print(d)
        #zhen = d.shape[0]  # 一个文件中有多少行数据
        # print(zhen)

        #提取一行数据append到列表，然后进行下一个循环，遍历所有文件最终集合到一个列表存入
        data = (d.iloc[0]).tolist()  # 读取d的第0行数据并转换为list类型
        sheet1.append(data)

    w.save('../keypoint/' + video_name[:-4] + '.xlsx')

    print('\n     ' + '文件共计 ' + str(video_num))
    print('\n     ' + str(n) + '已提取完成')
    if video_num - n > 0:
        m = n + 1
        print('     下一个提取 ' + str(m))
    else:
        print('     全部提取完成')




















