import pandas as pd
import numpy as np
import os
from tqdm import tqdm


def cosine_similarity(x, y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom


if __name__ == '__main__':
    person1_list = pd.read_csv(r'D:/PYproject/cnn+lstm/probe.csv')
    person2_list = pd.read_csv(r'D:/PYproject/cnn+lstm/gallery.csv')
    root = r'D:/PYproject/cnn+lstm/Feature/'
    similarity_list = []
    header = ["person1", "person2", "similarity"]


    read_data1 = person1_list.iloc[:, 0:2]
    read_data2 = person2_list.iloc[:, 0:2]

    for i in tqdm(range(len(read_data1))):
        similarity_list = []
        for j in range(len(read_data2)):
            file1_name = os.path.join(root, str(read_data1.iloc[i, 1]) + ".csv")
            file2_name = os.path.join(root, str(read_data2.iloc[j, 1]) + ".csv")
            person1_data = np.array(pd.read_csv(file1_name, header=None))
            person2_data = np.array(pd.read_csv(file2_name, header=None))
            # similarity = cosine_similarity(person1_data, person2_data).astype(float)
            similarity = float(cosine_similarity(person1_data, person2_data))
            similarity_list.append([read_data1.iloc[i, 0], read_data2.iloc[j, 0], similarity])
        similarity_result = pd.DataFrame(columns=header, data=similarity_list)
        # print(i, "/", len(read_data1), "\n", j, "/", len(read_data2))
        # np.savetxt("result_{}.csv".format(read_data1.iloc[i, 0]),similarity_list,fmt="")
        similarity_result.to_csv("./result/result_{}.csv".format(read_data1.iloc[i, 0]), encoding='gbk')
