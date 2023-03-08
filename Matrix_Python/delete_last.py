import pandas as pd
import csv
import sys
# 删除特征矩阵二的最后一行（最新的有问题的一行）
path = sys.argv[1]
data = pd.read_csv(path)
ll = len(data)
data_new = data.drop([ll - 1])
data_new.to_csv(path, index=0)
print("删除成功！")
