import os 

output="E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output\\video"
output1="E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video"
matrix_v1="E:\\workspace-sts\\Gait\\Matrix\\video1"
matrix_v2="E:\\workspace-sts\\Gait\\Matrix\\video2"
picture1="E:\\workspace-sts\\Gait\\picture\\video1"
picture2="E:\\workspace-sts\\Gait\\picture\\video2"

def empty(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

if __name__ == '__main__':
    empty(output)
    empty(output1)
    empty(matrix_v1)
    empty(matrix_v2)
    empty(picture1)
    empty(picture2)