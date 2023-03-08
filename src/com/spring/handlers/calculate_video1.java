package com.spring.handlers;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class calculate_video1 {
	
	private static final String FilePath1 = "E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video";//video1提取的关节点文件所在路径
	private static final String path_matrix_out1 = "E:\\workspace-sts\\Gait\\Matrix\\video1";//video1输出文件路径
	private static final String matrix_m_out11 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\output_one.csv";//特征矩阵中间结果
	private static final String matrix_m_out21 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\output_two.csv";
	private static final String matrix_f_out11 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\real_one.csv";//最终的特征矩阵
	private static final String matrix_f_out21 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\real_two.csv";
	static int[] p_name = new int[50];//存对应顺序图片序列
	
	
/*	//清空文件夹
	public static boolean deleteDir(String path){
		File file = new File(path);
		if(!file.exists()){//判断是否待删除目录是否存在
			System.err.println("The dir are not exists!");
			return false;
		}
		
		String[] content = file.list();//取得当前目录下所有文件和文件夹
		for(String name : content){
			File temp = new File(path, name);
			if(temp.isDirectory()){//判断是否是目录
				deleteDir(temp.getAbsolutePath());//递归调用，删除目录里的内容
				temp.delete();//删除空目录
			}else{
				if(!temp.delete()){//直接删除文件
					System.err.println("Failed to delete " + name);
				}
			}
		}
		System.out.println("删除成功！");
		return true;
	}*/
	
	//计算矩阵
	public static void calculate_matrix() {

		//生成两个矩阵表
		cal_matrix.create(path_matrix_out1);
		//测试
		int num = cal_matrix.csv_num(FilePath1,".csv");//csv文件数
		int start = cal_matrix.csv_start(FilePath1,".csv"); //csv开始帧数
		//计算中间特征矩阵一
		for(int i=0+start;i<num+start;i++)
			cal_matrix.compute_one(i,FilePath1,matrix_m_out11);
		System.out.println("video1中间特征矩阵一计算完毕！");
		
		//计算中间特征矩阵二
		int i = 0+start;
		int n = 1+start;
		while(n<num+start) {
			int result = cal_matrix.compute_Two(i,n,FilePath1,matrix_m_out21);
			if(result == 0)
				{
				cal_matrix.delete_Last(matrix_m_out21);
				n++;
				}
			else if(result == 1)
				{
				i = n;
				n++;
				}

		}
		System.out.println("video1中间特征矩阵二计算完毕！");
		
		//计算真正特征矩阵二
		cal_matrix.cal_real2(matrix_m_out21,matrix_f_out21,path_matrix_out1);
		System.out.println("video1最终特征矩阵二计算完毕！");
		//计算真正特征矩阵一
		p_name = cal_matrix.cal_real1(matrix_m_out11,matrix_f_out11,path_matrix_out1,matrix_f_out21);
		System.out.println("video1最终特征矩阵一50帧数：");
		for(int s=0;s<50;s++) {
			System.out.println(p_name[s]);
		}
		
		System.out.println("video1最终特征矩阵一计算完毕！");
		
		//转移矩阵对应的50张骨架图
		String path_in = "E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video";//视频1生成的关节点图片所在路径
		String path_out = "E:\\workspace-sts\\Gait\\picture\\video1";
		try {
			File f = new File(path_in);
			if (f.isDirectory()) {
				File[] fList = f.listFiles();
				for (int j = 0; j < fList.length; j++) {
					File file = fList[j];
					if (file.isFile()) { // 在这里加判断 按顺序判断是不是 s[]里的 这样就能按顺序复制过去 复制改名字比较难改
						if (file.getName().endsWith(".png")) {
							String now = file.getName();//方便读代码吧
							 System.out.println("now当前是"+now);
							
				 for(int p_n =0;p_n<50;p_n++) { //抽和特2对应的50帧

					 String s = "frame"+p_name[p_n]+"_keypoints.png";
					 System.out.println("s当前是"+s);
					 if(s.equalsIgnoreCase(now))
					 { 		 
						 System.out.println("开始复制了");
						 File result = new File(path_out+"\\"+s);//需要复制到的路径，以及图片的新命名+格式
						 FileInputStream input = new FileInputStream(path_in+"\\"+now);//需要复制的原图的路径+图片名+ .png(这是该图片的格式)
						 FileOutputStream out = new FileOutputStream(result);
						 byte[] buffer = new byte[100];//一个容量，相当于打水的桶，可以自定义大小
						 int hasRead = 0;
						 while ((hasRead = input.read(buffer)) > 0) {
							 out.write(buffer, 0, hasRead);//0：表示每次从0开始
						 	}
						 System.out.println(result.getAbsolutePath());
						 input.close();//关闭
						 out.close();
						 break;
					 	}
				 	}
						}
					}
				}
			}
		} catch (Exception e) {
		}
}


	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
