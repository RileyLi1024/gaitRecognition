package com.spring.handlers;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class calculate_video1 {
	
	private static final String FilePath1 = "E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video";//video1��ȡ�Ĺؽڵ��ļ�����·��
	private static final String path_matrix_out1 = "E:\\workspace-sts\\Gait\\Matrix\\video1";//video1����ļ�·��
	private static final String matrix_m_out11 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\output_one.csv";//���������м���
	private static final String matrix_m_out21 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\output_two.csv";
	private static final String matrix_f_out11 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\real_one.csv";//���յ���������
	private static final String matrix_f_out21 = "E:\\workspace-sts\\Gait\\Matrix\\video1\\real_two.csv";
	static int[] p_name = new int[50];//���Ӧ˳��ͼƬ����
	
	
/*	//����ļ���
	public static boolean deleteDir(String path){
		File file = new File(path);
		if(!file.exists()){//�ж��Ƿ��ɾ��Ŀ¼�Ƿ����
			System.err.println("The dir are not exists!");
			return false;
		}
		
		String[] content = file.list();//ȡ�õ�ǰĿ¼�������ļ����ļ���
		for(String name : content){
			File temp = new File(path, name);
			if(temp.isDirectory()){//�ж��Ƿ���Ŀ¼
				deleteDir(temp.getAbsolutePath());//�ݹ���ã�ɾ��Ŀ¼�������
				temp.delete();//ɾ����Ŀ¼
			}else{
				if(!temp.delete()){//ֱ��ɾ���ļ�
					System.err.println("Failed to delete " + name);
				}
			}
		}
		System.out.println("ɾ���ɹ���");
		return true;
	}*/
	
	//�������
	public static void calculate_matrix() {

		//�������������
		cal_matrix.create(path_matrix_out1);
		//����
		int num = cal_matrix.csv_num(FilePath1,".csv");//csv�ļ���
		int start = cal_matrix.csv_start(FilePath1,".csv"); //csv��ʼ֡��
		//�����м���������һ
		for(int i=0+start;i<num+start;i++)
			cal_matrix.compute_one(i,FilePath1,matrix_m_out11);
		System.out.println("video1�м���������һ������ϣ�");
		
		//�����м����������
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
		System.out.println("video1�м����������������ϣ�");
		
		//�����������������
		cal_matrix.cal_real2(matrix_m_out21,matrix_f_out21,path_matrix_out1);
		System.out.println("video1�������������������ϣ�");
		//����������������һ
		p_name = cal_matrix.cal_real1(matrix_m_out11,matrix_f_out11,path_matrix_out1,matrix_f_out21);
		System.out.println("video1������������һ50֡����");
		for(int s=0;s<50;s++) {
			System.out.println(p_name[s]);
		}
		
		System.out.println("video1������������һ������ϣ�");
		
		//ת�ƾ����Ӧ��50�ŹǼ�ͼ
		String path_in = "E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video";//��Ƶ1���ɵĹؽڵ�ͼƬ����·��
		String path_out = "E:\\workspace-sts\\Gait\\picture\\video1";
		try {
			File f = new File(path_in);
			if (f.isDirectory()) {
				File[] fList = f.listFiles();
				for (int j = 0; j < fList.length; j++) {
					File file = fList[j];
					if (file.isFile()) { // ��������ж� ��˳���ж��ǲ��� s[]��� �������ܰ�˳���ƹ�ȥ ���Ƹ����ֱȽ��Ѹ�
						if (file.getName().endsWith(".png")) {
							String now = file.getName();//����������
							 System.out.println("now��ǰ��"+now);
							
				 for(int p_n =0;p_n<50;p_n++) { //�����2��Ӧ��50֡

					 String s = "frame"+p_name[p_n]+"_keypoints.png";
					 System.out.println("s��ǰ��"+s);
					 if(s.equalsIgnoreCase(now))
					 { 		 
						 System.out.println("��ʼ������");
						 File result = new File(path_out+"\\"+s);//��Ҫ���Ƶ���·�����Լ�ͼƬ��������+��ʽ
						 FileInputStream input = new FileInputStream(path_in+"\\"+now);//��Ҫ���Ƶ�ԭͼ��·��+ͼƬ��+ .png(���Ǹ�ͼƬ�ĸ�ʽ)
						 FileOutputStream out = new FileOutputStream(result);
						 byte[] buffer = new byte[100];//һ���������൱�ڴ�ˮ��Ͱ�������Զ����С
						 int hasRead = 0;
						 while ((hasRead = input.read(buffer)) > 0) {
							 out.write(buffer, 0, hasRead);//0����ʾÿ�δ�0��ʼ
						 	}
						 System.out.println(result.getAbsolutePath());
						 input.close();//�ر�
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
