# 计算特征矩阵一
import math
import pandas as pd
import csv
import sys


def main():
    # i是当前访问第几帧 写入第i+1行
    # 参数从下标1开始取
    i = sys.argv[1]
    path_in = sys.argv[2]
    path_out = sys.argv[3]
    a = "frame" + i + "_keypoints.csv"
    data = pd.read_csv(filepath_or_buffer=path_in+"\\"+a)
    #print(data)
    # print(data.columns)
    #print(data.values)
    # print(data.shape)
    # print(len(data))

    # print(data)
    # 计算角度 特征举证一的计算 a1-a44
    # 关节点0与1,15,8之间的夹角(编号9与8、7、0) 第一个计算结果手算核对无误
    a1 = abs(data['z'][9] - data['z'][8]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][8]), 2) + math.pow((data['y'][9] - data['y'][8]), 2))
    a2 = abs(data['z'][9] - data['z'][7]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][7]), 2) + math.pow((data['y'][9] - data['y'][7]), 2))
    a3 = abs(data['z'][9] - data['z'][0]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][0]), 2) + math.pow((data['y'][9] - data['y'][0]), 2))
    # 关节点0与9-14之间的夹角(编号9与4、5、6、1、2、3)
    a4 = abs(data['z'][9] - data['z'][4]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][4]), 2) + math.pow((data['y'][9] - data['y'][4]), 2))
    a5 = abs(data['z'][9] - data['z'][5]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][5]), 2) + math.pow((data['y'][9] - data['y'][5]), 2))
    a6 = abs(data['z'][9] - data['z'][6]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][6]), 2) + math.pow((data['y'][9] - data['y'][6]), 2))
    a7 = abs(data['z'][9] - data['z'][1]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][1]), 2) + math.pow((data['y'][9] - data['y'][1]), 2))
    a8 = abs(data['z'][9] - data['z'][2]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][2]), 2) + math.pow((data['y'][9] - data['y'][2]), 2))
    a9 = abs(data['z'][9] - data['z'][3]) / math.sqrt(
        math.pow((data['x'][9] - data['x'][3]), 2) + math.pow((data['y'][9] - data['y'][3]), 2))
    # 关节点1与9-14之间的夹角(编号8与4、5、6、1、2、3)
    a10 = abs(data['z'][8] - data['z'][4]) / math.sqrt(
        math.pow((data['x'][8] - data['x'][4]), 2) + math.pow((data['y'][8] - data['y'][4]), 2))
    a11 = abs(data['z'][8] - data['z'][5]) / math.sqrt(
        math.pow((data['x'][8] - data['x'][5]), 2) + math.pow((data['y'][8] - data['y'][5]), 2))
    a12 = abs(data['z'][8] - data['z'][6]) / math.sqrt(
        math.pow((data['x'][8] - data['x'][6]), 2) + math.pow((data['y'][8] - data['y'][6]), 2))
    a13 = abs(data['z'][8] - data['z'][1]) / math.sqrt(
        math.pow((data['x'][8] - data['x'][1]), 2) + math.pow((data['y'][8] - data['y'][1]), 2))
    a14 = abs(data['z'][8] - data['z'][2]) / math.sqrt(
        math.pow((data['x'][8] - data['x'][2]), 2) + math.pow((data['y'][8] - data['y'][2]), 2))
    a15 = abs(data['z'][8] - data['z'][3]) / math.sqrt(
        math.pow((data['x'][8] - data['x'][3]), 2) + math.pow((data['y'][8] - data['y'][3]), 2))
    # 关节点15与9-14之间的夹角(编号7与4、5、6、1、2、3)
    a16 = abs(data['z'][7] - data['z'][4]) / math.sqrt(
        math.pow((data['x'][7] - data['x'][4]), 2) + math.pow((data['y'][7] - data['y'][4]), 2))
    a17 = abs(data['z'][7] - data['z'][5]) / math.sqrt(
        math.pow((data['x'][7] - data['x'][5]), 2) + math.pow((data['y'][7] - data['y'][5]), 2))
    a18 = abs(data['z'][7] - data['z'][6]) / math.sqrt(
        math.pow((data['x'][7] - data['x'][6]), 2) + math.pow((data['y'][7] - data['y'][6]), 2))
    a19 = abs(data['z'][7] - data['z'][1]) / math.sqrt(
        math.pow((data['x'][7] - data['x'][1]), 2) + math.pow((data['y'][7] - data['y'][1]), 2))
    a20 = abs(data['z'][7] - data['z'][2]) / math.sqrt(
        math.pow((data['x'][7] - data['x'][2]), 2) + math.pow((data['y'][7] - data['y'][2]), 2))
    a21 = abs(data['z'][7] - data['z'][3]) / math.sqrt(
        math.pow((data['x'][7] - data['x'][3]), 2) + math.pow((data['y'][7] - data['y'][3]), 2))
    # 关节点8与9-14之间的夹角(编号0与4、5、6、1、2、3)
    a22 = abs(data['z'][0] - data['z'][4]) / math.sqrt(
        math.pow((data['x'][0] - data['x'][4]), 2) + math.pow((data['y'][0] - data['y'][4]), 2))
    a23 = abs(data['z'][0] - data['z'][5]) / math.sqrt(
        math.pow((data['x'][0] - data['x'][5]), 2) + math.pow((data['y'][0] - data['y'][5]), 2))
    a24 = abs(data['z'][0] - data['z'][6]) / math.sqrt(
        math.pow((data['x'][0] - data['x'][6]), 2) + math.pow((data['y'][0] - data['y'][6]), 2))
    a25 = abs(data['z'][0] - data['z'][1]) / math.sqrt(
        math.pow((data['x'][0] - data['x'][1]), 2) + math.pow((data['y'][0] - data['y'][1]), 2))
    a26 = abs(data['z'][0] - data['z'][2]) / math.sqrt(
        math.pow((data['x'][0] - data['x'][2]), 2) + math.pow((data['y'][0] - data['y'][2]), 2))
    a27 = abs(data['z'][0] - data['z'][3]) / math.sqrt(
        math.pow((data['x'][0] - data['x'][3]), 2) + math.pow((data['y'][0] - data['y'][3]), 2))
    # 下肢关节点之间的夹角 关节点9与10、11(编号4与5、6)关节点10与11(5与6)关节点12与13、14(1与2、3)关节点13与14(2与3)
    a28 = abs(data['z'][4] - data['z'][5]) / math.sqrt(
        math.pow((data['x'][4] - data['x'][5]), 2) + math.pow((data['y'][4] - data['y'][5]), 2))
    a29 = abs(data['z'][4] - data['z'][6]) / math.sqrt(
        math.pow((data['x'][4] - data['x'][6]), 2) + math.pow((data['y'][4] - data['y'][6]), 2))
    a30 = abs(data['z'][5] - data['z'][6]) / math.sqrt(
        math.pow((data['x'][5] - data['x'][6]), 2) + math.pow((data['y'][5] - data['y'][6]), 2))
    a31 = abs(data['z'][1] - data['z'][2]) / math.sqrt(
        math.pow((data['x'][1] - data['x'][2]), 2) + math.pow((data['y'][1] - data['y'][2]), 2))
    a32 = abs(data['z'][1] - data['z'][3]) / math.sqrt(
        math.pow((data['x'][1] - data['x'][3]), 2) + math.pow((data['y'][1] - data['y'][3]), 2))
    a33 = abs(data['z'][2] - data['z'][3]) / math.sqrt(
        math.pow((data['x'][2] - data['x'][3]), 2) + math.pow((data['y'][2] - data['y'][3]), 2))
    # 重力铅垂线方向 关节点1与9-14(编号8与4、5、6、1、2、3) 第一个计算结果手算核对无误
    a34 = abs(data['z'][8] - data['z'][4]) / abs(data['x'][8] - data['x'][4])
    a35 = abs(data['z'][8] - data['z'][5]) / abs(data['x'][8] - data['x'][5])
    a36 = abs(data['z'][8] - data['z'][6]) / abs(data['x'][8] - data['x'][6])
    a37 = abs(data['z'][8] - data['z'][1]) / abs(data['x'][8] - data['x'][1])
    a38 = abs(data['z'][8] - data['z'][2]) / abs(data['x'][8] - data['x'][2])
    a39 = abs(data['z'][8] - data['z'][3]) / abs(data['x'][8] - data['x'][3])
    # 身体比例约束
    # 身高步长比 公式关节点顺序0 11 14(编号9 6 3)
    a40 = abs(data['z'][9]) / math.sqrt(
        math.pow((data['x'][6] - data['x'][3]), 2) + math.pow((data['y'][6] - data['y'][3]), 2))
    # 重心步长比 公式关节点顺序8 11 14(编号0 6 3)
    a41 = abs(data['z'][0]) / math.sqrt(
        math.pow((data['x'][6] - data['x'][3]), 2) + math.pow((data['y'][6] - data['y'][3]), 2))
    # 身高重心比 关节点0/8(编号9/0)
    a42 = abs(data['z'][9]) / abs(data['z'][0])
    # 右腿长比 关节点12/13(编号1/2)
    a43 = abs(data['z'][1]) / abs(data['z'][2])
    # 左腿长比 关节点9/10(编号4/5)
    a44 = abs(data['z'][4]) / abs(data['z'][5])

    # 导出 导出表提前清空
    filename = a.replace('.csv', '')
    matrix1 = [filename, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,
               a11, a12, a13, a14, a15, a16, a17, a18, a19,
               a20, a21, a22, a23, a24, a25, a26, a27, a28,
               a29, a30, a31, a32, a33, a34, a35, a36, a37,
               a38, a39, a40, a41, a42, a43, a44]

    # names = ['filename', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
    #          'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19',
    #          'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28',
    #          'a29', 'a30', 'a31', 'a32', 'a33', 'a34', 'a35', 'a36', 'a37',
    #          'a38', 'a39', 'a40', 'a41', 'a42', 'a43', 'a44']

    # test = pd.DataFrame(columns=names)
    # test.to_csv('output_one.csv', index=False)
    # f = open("output_one.csv", 'a', newline='')
    # writer = csv.writer(f)
    # writer.writerow(matrix)
    # f.close()
    file = open(path_out)
    reader = csv.reader(file)
    original = list(reader)
    file1 = open(path_out, 'w', newline='')
    content = csv.writer(file1)
    for row in original:
        content.writerow(row)
    content.writerow(matrix1)
    file.close()
    file1.close()
   # print("调1成功！")


if __name__ == '__main__':
    main()
