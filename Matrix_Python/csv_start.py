import os
import sys


def get_filename(path, filetype):  # 输入路径、文件类型例如'.csv'
    name = []  # 存所有数组名
    for root, dirs, files in os.walk(path):
        for i in files:
            if os.path.splitext(i)[1] == filetype:
                name.append(i)
    # print(len(name))  # 返回csv文件数
    # 提取 文件名中的数字序号
    num = []
    for i in range(len(name)):
        # 提取出filename中的序号
        s = name[i]
        index = s.index('e') + 1
        sen = s[index:].replace('_keypoints.csv', '')
        num.append(sen)
    num = list(map(int, num))  # 将字符串数组转换成整形数组
    num.sort()  # 升序排序
    print(num[0])  # 返回最小的数字 这就是最开始一帧
    # 因为生成的csv文件开始帧数一定是最小的 并且都是连续的 所以从获取的名字中找到最小的那个帧数的数字 min_val+个数就是需要循环调用求特一几次
    # min_val = name[0] # 擂主
    # for i in range(len(name)):
    #     if


if __name__ == '__main__':
    path = sys.argv[1]
    filetype = sys.argv[2]
    get_filename(path, filetype)
