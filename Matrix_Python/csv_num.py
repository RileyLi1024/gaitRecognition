import os
import sys


def get_filename(path, filetype):  # 输入路径、文件类型例如'.csv'
    name = []  # 存所有数组名
    for root, dirs, files in os.walk(path):
        for i in files:
            if os.path.splitext(i)[1] == filetype:
                name.append(i)
    print(len(name))  # 返回csv文件数

if __name__ == '__main__':
    path = sys.argv[1]
    filetype = sys.argv[2]
    get_filename(path, filetype)