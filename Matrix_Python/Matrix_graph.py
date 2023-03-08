import os
import pandas as pd
import csv
import numpy as np


# 读取指定文件夹下的所有csv文件
# 递归获取.csv文件存入到list1
# 将所有文件的路径放入到listcsv列表中
def list_dir(file_dir):
    # list_csv = []
    dir_list = os.listdir(file_dir)
    for cur_file in dir_list:
        path = os.path.join(file_dir, cur_file)
        # 判断是文件夹还是文件
        if os.path.isfile(path):
            # print("{0} : is file!".format(cur_file))
            dir_files = os.path.join(file_dir, cur_file)
        # 判断是否存在.csv文件，如果存在则获取路径信息写入到list_csv列表中
        if os.path.splitext(path)[1] == '.csv':
            csv_file = os.path.join(file_dir, cur_file)
            # print(os.path.join(file_dir, cur_file))
            # print(csv_file)
            list_csv.append(csv_file)
        if os.path.isdir(path):
            # print("{0} : is dir".format(cur_file))
            # print(os.path.join(file_dir, cur_file))
            list_dir(path)
    return list_csv


# 重命名帧文件
def rename(path):
    for i in sorted(os.listdir(path)):
        i_path = os.path.join(path, i)
        d = i.split("_")
        d1 = d[0].split("e")
        a = d1[0] + 'e' + d1[1].zfill(3) + '_' + d[1]
        a_path = os.path.join(path, a)
        os.rename(i_path, a_path)
        os.listdir(path)
    print("rename!")


# 生成新的csv文件
def create_csv(filepath):
    # 创建新表
    names1 = ['filename', 'Head_x', 'Head_y', 'Head_z', 'Thorax_x', 'Thorax_y', 'Thorax_z', 'LShoulder_x',
              'LShoulder_y', 'LShoulder_z', 'LElbow_x',
              'LElbow_y', 'LElbow_z', 'LWrist_x', 'LWrist_y', 'LWrist_z', 'RShoulder_x', 'RShoulder_y', 'RShoulder_z',
              'RElbow_x',
              'RElbow_y', 'RElbow_z', 'RWrist_x', 'RWrist_y', 'RWrist_z', 'Hip_x', 'Hip_y', 'Hip_z', 'LHip_x', 'LHip_y',
              'LHip_z',
              'LKnee_x', 'LKnee_y', 'LKnee_z', 'LFoot_x', 'LFoot_y', 'LFoot_z', 'RHip_x', 'RHip_y', 'RHip_z', 'RKnee_x',
              'RKnee_y', 'RKnee_z',
              'RFoot_x', 'RFoot_y', 'RFoot_z', 'Spine_x', 'Spine_y', 'Spine_z']
    data1 = pd.DataFrame(columns=names1).to_csv(filepath, index=False)
    person = filepath.split('person')[1].split('.')[0].zfill(3)
    # 挨个读取csv文件夹
    for i in range(len(list_csv)):
        path = list_csv[i]
        # print(a)
        a = np.loadtxt(path, dtype=str, delimiter=',')
        # print(a)
        # 处理frame每一帧的csv文件里的数据，只要纯数字 初始文件规模为17X6
        # 删除第一行，第1,2列和最后一列（最后一列为空）
        a = np.delete(a, 0, axis=0)
        a = np.delete(a, [0, 1], axis=1)
        # 还剩4列（最后一列为空,也要删去）
        a = np.delete(a, 3, axis=1)
        # 调整关节点数据对应的位置
        id = './' + person + '-nm-01-000/'+str(i).zfill(3) +'.jpg'
        matrix = [id, a[9][0], a[9][1], a[9][2], a[8][0], a[8][1], a[8][2],
                  a[10][0], a[10][1], a[10][2], a[11][0], a[11][1], a[11][2],
                  a[12][0], a[12][1], a[12][2], a[13][0], a[13][1], a[13][2],
                  a[14][0], a[14][1], a[14][2], a[15][0], a[15][1], a[15][2],
                  a[0][0], a[0][1], a[0][2], a[4][0], a[4][1], a[4][2], a[5][0],
                  a[5][1], a[5][2], a[6][0], a[6][1], a[6][2], a[1][0], a[1][1],
                  a[1][2], a[2][0], a[2][1], a[2][2], a[3][0], a[3][1], a[3][2],
                  a[7][0], a[7][1], a[7][2]]
        # print("matrix:")
        # print(matrix)

        file = open(filepath)
        reader = csv.reader(file)
        original = list(reader)
        file1 = open(filepath, 'w', newline='')
        content = csv.writer(file1)
        for row in original:
            content.writerow(row)
        content.writerow(matrix)
        file.close()
        file1.close()


if __name__ == '__main__':
    data_path1 = "E:/workspace-sts/Gait/Matrix/GaitGraph/person1.csv"
    data_path2 = "E:/workspace-sts/Gait/Matrix/GaitGraph/person2.csv"
    # person1
    paths1 = r'E:\workspace-sts\Gait\Pose3Dkeypoints\output1\video'
    rename(paths1)
    list_csv = []
    list_dir(file_dir=paths1)
    print(list_csv)
    create_csv(data_path1)
    # person2
    paths2 = r'E:\workspace-sts\Gait\Pose3Dkeypoints\output\video'
    rename(paths2)
    list_csv = []
    list_dir(file_dir=paths2)
    print(list_csv)
    create_csv(data_path2)
