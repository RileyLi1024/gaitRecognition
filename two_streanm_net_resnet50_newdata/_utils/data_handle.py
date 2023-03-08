import os
root = r"C:\705_user\wangyunjeff\Code\2_Project\two_stream_net2\two_stream_net\data\第二方案数据更新\步态新样本\data2"
files = os.listdir(root)

for filename in files:
    portion = os.path.splitext(filename)
    # 如果后缀是.dat
    if portion[1] == ".CSV":
        # 重新组合文件名和后缀名

        newname = portion[0] + ".csv"
        os.rename(os.path.join(root,filename), os.path.join(root,newname))