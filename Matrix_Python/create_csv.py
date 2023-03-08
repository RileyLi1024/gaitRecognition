import pandas as pd
import sys

def creat(path):
    names1 = ['filename', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
              'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19',
              'a20', 'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28',
              'a29', 'a30', 'a31', 'a32', 'a33', 'a34', 'a35', 'a36', 'a37',
              'a38', 'a39', 'a40', 'a41', 'a42', 'a43', 'a44']
    data1 = pd.DataFrame(columns=names1).to_csv(path_or_buf=path+"\\output_one.csv", index=False)

    names2 = ['number','filename', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13',
              'x14', 'x15', 'y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 'y10', 'y11', 'y12', 'y13',
              'y14', 'y15', 'z0', 'z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10', 'z11', 'z12', 'z13',
              'z14', 'z15']
    data2 = pd.DataFrame(columns=names2).to_csv(path_or_buf=path+"\\output_two.csv", index=False)
    print("成功创建啦！")


if __name__ == '__main__':
    path = sys.argv[1]
    creat(path)
    print(1)