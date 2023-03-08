import os
import os.path as osp

path1 = "E:\\workspace-sts\\Gait\\picture\\video1"
path2 = "E:\\workspace-sts\\Gait\\picture\\video2"


def rename(path):
    for i in sorted(os.listdir(path)):
        i_path = os.path.join(path, i)
        d = i.split("_")
        d1 = d[0].split("e")
        a = d1[0] + 'e' + d1[1].zfill(3) + '_' + d[1]
        a_path = os.path.join(path, a)
        os.rename(i_path, a_path)
        os.listdir(path)
        print("rename!")


if __name__ == '__main__':
    rename(path1)
    rename(path2)
    print(1)
