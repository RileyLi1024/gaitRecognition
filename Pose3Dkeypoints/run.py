import argparse
import os
import sys
import shutil
import cv2

# sys.path.append("E:/user/lj/3DPose-keypoints/3d-pose/src")
sys.path.append("3d-pose/src")
from openpose_3dpose_sandbox import twoDcoordsToThreeDcoords

if len(sys.argv) < 3:
    print("print type command line parameters...")

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str, help="input directory")
parser.add_argument("type", type=str, help="i(image) or v(video)")
args = parser.parse_args()


def main():
    imagePath = ''
    videoPath = ''
    if args.type == 'i':
        imagePath = args.path

        if os.path.exists(imagePath) is not True:
            return

        twoDposePath = imagePath + '/' + "2dPose"
        if os.path.exists(twoDposePath) is True:
            shutil.rmtree(twoDposePath)
        os.makedirs(twoDposePath)

        orignalPath = os.getcwd()
        os.chdir("openpose/")
        openPoseCmd = "bin/OpenPoseDemo.exe --image_dir " +\
                      "../" + imagePath + " --write_json " + "../" + twoDposePath
        openPoseCmd = openPoseCmd.replace('/', "\\")
        os.system(openPoseCmd)
        os.chdir(orignalPath)
        os.chdir("./3d-pose")
        #print("\n\n\n" + os.getcwd() + "\n\n")
        outputPath = "../output/image/"
        if os.path.exists(outputPath) is True:
            shutil.rmtree(outputPath)
        os.makedirs(outputPath)
        twoDcoordsToThreeDcoords("../" + twoDposePath, outputPath)


    elif args.type == 'v':
        videoPath = args.path
        if os.path.exists(videoPath) is not True:
            return
        print(videoPath)
        cvtImageOutPath = "./input/video/tmp/image/"

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
        os.chdir("openpose/")
        openPoseCmd = "bin/OpenPoseDemo.exe --image_dir " +\
                      "../" + cvtImageOutPath + " --write_json " + "../"\
                        + cvtImageOutPath + "../2dPose"
        openPoseCmd = openPoseCmd.replace('/', "\\")
        os.system(openPoseCmd)
        os.chdir(orignalPath)
        os.chdir("./3d-pose")
        outputPath = "../output/video/"
        if os.path.exists(outputPath) is True:
            shutil.rmtree(outputPath)
        os.makedirs(outputPath)
        twoDcoordsToThreeDcoords("../" + cvtImageOutPath + "../2dPose",
                                 outputPath)


    else:
        print("print type correct command line parameters...")
        return

if __name__ == "__main__":
    main()