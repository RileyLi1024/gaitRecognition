import pandas as pd
import sys

def main():
    path_in = sys.argv[1] # 中间特一路径
    path_out = sys.argv[2] # 最终特一路径
    path = sys.argv[3] # 结果输出路径
    path2 = sys.argv[4] # 最终特二路径 根据特二选特一
    # 按照特征矩阵二的50帧选出特征矩阵一的50帧
    real_2 = pd.read_csv(path2)

    # 得到 特二里 framex_y 中的y 按y找特一
    l = list()
    for i in range(50):  # 这里肯定是50 因为已知real_two里面就50帧
        s = real_2['filename'][i]
        index = s.index('-') + 1
        print(s[index:])
        l.append(s[index:])
    #print(l)

    names1 = ['filename', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
              'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19',
              'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28',
              'a29', 'a30', 'a31', 'a32', 'a33', 'a34', 'a35', 'a36', 'a37',
              'a38', 'a39', 'a40', 'a41', 'a42', 'a43', 'a44']
    data1 = pd.DataFrame(columns=names1).to_csv(path_or_buf=path+"\\real_one.csv", index=False)

    content = []
    for i in range(50):
        s = "frame" + str(l[i]) + "_keypoints"
        with open(path_in, 'r') as f1:
            lines = f1.readlines()  # 读取一行
            for line in lines:
                new_list = line.split(',')  # 切片分段 以,为分隔符 这样就可以吧Line一行一行的 分成[‘’ ‘’]的了
                if new_list[0] == s:  # 看frameY_keypoints是否想等了 相等就说明这这一帧是对应的特一 new_list[0]对应第一列的filename
                    content.append(line)
                    with open(path_out, 'a+') as f2:
                        f2.writelines(line)


if __name__ == '__main__':
    main()
