# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:09:35 2020

@author: lijing
"""

import sys
import numpy as np
import math
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import StandardScaler
# from keras.models import Model
# from keras.models import load_model
# import CNN as CNNmodel
# import cosSimilarity as cos


import os
# import importlib, sys

# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

# importlib.reload(sys)

# os.environ['CUDA_VISIBLE_DEVICES'] = '/gpu:0'


# def cosine_similarity(x, y):
#     num = np.dot(x, y.T)
#     denom = np.linalg.norm(x) * np.linalg.norm(y)
#     if (x == y).all():
#         result = 1.0
#     elif denom == 0:
#         result = 0.0
#     else:
#         result = num / denom
#     return result

def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom
if __name__ == '__main__':
    while True:
        person1 = input('请输出person1:')
        person2 = input('请输出person2:')
        x = np.array(pd.read_csv(r'D:/PYproject/cnn+lstm/Feature/{}.csv'.format(person1),header=None))
        y = np.array(pd.read_csv(r'D:/PYproject/cnn+lstm/Feature/{}.csv'.format(person2),header=None))
        print(cosine_similarity(x,y))