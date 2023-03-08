import re

import numpy as np
import pandas as pd
import sys


def cosine_similarity(x, y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)

    return float(num / denom)


if __name__ == '__main__':
    matrix1_p = sys.argv[1]
    # 待判定的视频的特征向量路径
    data1 = pd.read_csv("E:\\workspace-sts\\Gait\\Matrix\\video2\\matrix2.txt",
                        header=None)  # 读取TXT:逗号分隔
    # print(data1[0:])
    vector1 = np.array(data1[0:])
   # print(vector1)

    data2 = pd.read_csv(matrix1_p,
                        header=None)  # 读取TXT:逗号分隔
    # print(data2[0:])
    vector2 = np.array(data2[0:])
   # print(vector2)
    sim = cosine_similarity(vector1, vector2)
    print(sim)
