import itertools
import pandas as pd
import csv
import sys


# 筛选50帧特征矩阵二
def main():
    path_in = sys.argv[1]
    path_out = sys.argv[2]
    path = sys.argv[3]

    data = pd.read_csv(filepath_or_buffer=path_in)
    num = len(data)
    # print(num)
    # print(data['x0'][0])
    # 得到了y14-y11值最小且后面还有50帧的这一帧的序号
    min_val = abs(data['y14'][0] - data['y11'][0])  # 用来存最小值 擂主
    number = 0  # 存最小值对应的序号
    for i in range(num):
        n = num - i  # 包括当前帧往后一共还有多少帧
        if n >= 50 and (i + 1) <= num:  # 确保能取到50帧
            # print("这是n:" + str(n))
            dif = abs(data['y14'][i] - data['y11'][i])
            if dif < min_val:
                min_val = dif
                number = data['number'][i]
                print("这是最小值：" + str(min_val))
                print("最小值对应序号：")
                print(number)

    names2 = ['number', 'filename', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12',
              'x13',
              'x14', 'x15', 'y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13',
              'y14', 'y15', 'z0', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10', 'z11', 'z12', 'z13',
              'z14', 'z15']

    data2 = pd.DataFrame(columns=names2).to_csv(path_or_buf=path + "\\real_two.csv", index=False)
    # 生成的表总是间隔空一行
    file_in = open(path_in, 'r')
    file_out = open(path_out, 'a+')
    f_input = csv.reader(file_in)
    f_output = csv.writer(file_out)
    f_output.writerows(itertools.islice(f_input, number + 1, number + 51))  # 就是这么个写法 跟起始有点关系 这里是 取number及之后一共20个
    file_in.close()
    file_out.close()
    # 删除空行
    with open(path_out, 'rt')as f_in:  # 读有空行的csv文件，舍弃空行
        lines = ''
        for line in f_in:
            if line != '\n':
                lines += line
    with open(path_out, 'wt')as f_out:  # 再次文本方式写入，不含空行
        f_out.write(lines)


if __name__ == '__main__':
    main()
