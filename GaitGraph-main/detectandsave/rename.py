import os
import os.path as osp


if __name__ == "__main__":
    path ='test_detectresults_out'
    files = os.listdir(path)
    id = 0
    for file in files:
        file_path = osp.join(path, file)
        file_pathimg = osp.join(path, file, 'img')
        lenfile = len(os.listdir(file_pathimg))
        if lenfile < 10:
            continue
        id += 1
        os.rename(file_path, str(id).zfill(3))



