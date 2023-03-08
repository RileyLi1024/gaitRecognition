# 计算特征矩阵二 位移
import csv
import pandas as pd
import sys


def main():
    # 参数从1开始取
    i = sys.argv[1]
    #    i = 0
    num = sys.argv[2]
    path_in = sys.argv[3]
    path_out = sys.argv[4]
    a = "frame" + str(i) + "_keypoints.csv"
    b = "frame" + str(num) + "_keypoints.csv"
    data1 = pd.read_csv(filepath_or_buffer=path_in+"\\" + a)
    data2 = pd.read_csv(filepath_or_buffer=path_in+"\\" + b)
    # 关节点对应关系：0--9 1--8 2--10 3--11 4--12 5--13 6--14 7--15
    # 关节点--编号   8--0 9--4 10--5 11--6 12--1 13--2 14--3 15--7
    # 'x'坐标
    x0 = abs(data2['x'][9] - data1['x'][9])
    x1 = abs(data2['x'][8] - data1['x'][8])
    x2 = abs(data2['x'][10] - data1['x'][10])
    x3 = abs(data2['x'][11] - data1['x'][11])
    x4 = abs(data2['x'][12] - data1['x'][12])
    x5 = abs(data2['x'][13] - data1['x'][13])
    x6 = abs(data2['x'][14] - data1['x'][14])
    x7 = abs(data2['x'][15] - data1['x'][15])
    x8 = abs(data2['x'][0] - data1['x'][0])
    x9 = abs(data2['x'][4] - data1['x'][4])
    x10 = abs(data2['x'][5] - data1['x'][5])
    x11 = abs(data2['x'][6] - data1['x'][6])
    x12 = abs(data2['x'][1] - data1['x'][1])
    x13 = abs(data2['x'][2] - data1['x'][2])
    x14 = abs(data2['x'][3] - data1['x'][3])
    x15 = abs(data2['x'][7] - data1['x'][7])
    # 'y'坐标
    y0 = abs(data2['y'][9] - data1['y'][9])
    y1 = abs(data2['y'][8] - data1['y'][8])
    y2 = abs(data2['y'][10] - data1['y'][10])
    y3 = abs(data2['y'][11] - data1['y'][11])
    y4 = abs(data2['y'][12] - data1['y'][12])
    y5 = abs(data2['y'][13] - data1['y'][13])
    y6 = abs(data2['y'][14] - data1['y'][14])
    y7 = abs(data2['y'][15] - data1['y'][15])
    y8 = abs(data2['y'][0] - data1['y'][0])
    y9 = abs(data2['y'][4] - data1['y'][4])
    y10 = abs(data2['y'][5] - data1['y'][5])
    y11 = abs(data2['y'][6] - data1['y'][6])
    y12 = abs(data2['y'][1] - data1['y'][1])
    y13 = abs(data2['y'][2] - data1['y'][2])
    y14 = abs(data2['y'][3] - data1['y'][3])
    y15 = abs(data2['y'][7] - data1['y'][7])
    # 'z'坐标
    z0 = abs(data2['z'][9] - data1['y'][9])
    z1 = abs(data2['z'][8] - data1['y'][8])
    z2 = abs(data2['z'][10] - data1['y'][10])
    z3 = abs(data2['z'][11] - data1['y'][11])
    z4 = abs(data2['z'][12] - data1['y'][12])
    z5 = abs(data2['z'][13] - data1['y'][13])
    z6 = abs(data2['z'][14] - data1['y'][14])
    z7 = abs(data2['z'][15] - data1['y'][15])
    z8 = abs(data2['z'][0] - data1['y'][0])
    z9 = abs(data2['z'][4] - data1['y'][4])
    z10 = abs(data2['z'][5] - data1['y'][5])
    z11 = abs(data2['z'][6] - data1['y'][6])
    z12 = abs(data2['y'][1] - data1['y'][1])
    z13 = abs(data2['y'][2] - data1['y'][2])
    z14 = abs(data2['y'][3] - data1['y'][3])
    z15 = abs(data2['y'][7] - data1['y'][7])

    filename = "frame" + str(i) + "-" + str(num)
    number = number = pd.read_csv(path_out)
    matrix2 = [len(number), filename, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14,
               x15, y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15,
               z0, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15]
    # 无论有没有效 先给添加到表里
    file = open(path_out)
    reader = csv.reader(file)
    original = list(reader)
    file1 = open(path_out, 'w', newline='')
    content = csv.writer(file1)
    for row in original:
        content.writerow(row)
    content.writerow(matrix2)
    file.close()
    file1.close()

    # 判定这一帧是否有效 判断除y8的任何一个关节点都可
    if x0 == 0:
        flag = 0
    else :
        flag = 1
     # print(flag)
     # print("调2成功！")
    print(flag)


if __name__ == '__main__':
    main()
