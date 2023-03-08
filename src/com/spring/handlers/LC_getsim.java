package com.spring.handlers;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class LC_getsim {
	
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\pytorch\\python.exe";
	private static final String get_simm = "E:\\workspace-sts\\Gait\\cnn+lstm\\cal_sim.py";
	public static String main(String[] args){
		//�ҵ�����ע���û���Ƶ����������
		List<String> all_VectorName = new ArrayList<String>();
		all_VectorName=search("E:\\workspace-sts\\Gait\\Register");
		//���ε����������ƶȶ���py�ű����бȶ� ���ص��ǡ�double������ƶȣ���Ӧ��username��
		String sim_name = get_Sim(all_VectorName);
		String result =distinguish_name(sim_name);
		return result;
		}
			 
		public static List<String> search(String path)
		{
		System.out.println("����ע���б�");
		   File dir = new File(path);		 
		   List<String> all_VName = new ArrayList<String>(); //��������ע����Ƶ��������������
		   //������Ŀ¼
			if (dir.isDirectory()) 
			{ 
			  File[] fList = dir.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { 
				 if(file.getName().endsWith(".txt")&&file.getName().startsWith("matrix1")) {
					 System.out.println(file.getName());
			         all_VName.add(file.getName());	
				 }
			   }
			 } 
			
			} 
		   return all_VName;
		}
		
		public static String get_Sim(List<String> all_VName) {
			List<String> VectorPath = new ArrayList<String>();
			
			for (int i = 0; i < all_VName.size(); i++) {
				System.out.print("�����������б�"+all_VName.get(i) );
				VectorPath.add("E:\\workspace-sts\\Gait\\Register\\"+all_VName.get(i));
			}
			
			for (int j = 0; j < VectorPath.size(); j++) {
				System.out.print("��������·���б�"+VectorPath.get(j)+"\t");
			}
			
			//���ε���py�ű��õ����ƶȽ�� �����������˹�����  ���matrix_username_f1.csv ����ÿ������
			//���ú��鷳��һ��Usrnameһ�����ƶȽ���� ֱ���ҵ�����Ȼ��getnameȻ��_��Ϊ�ָ��� �ָ��username�����б���~~~
			Double sim = 0.0;
			String dis_name ="";
			System.out.println("�Ѿ�ע����û�����Ϊ��"+VectorPath.size());
			for (int i = 0;i<VectorPath.size(); i++) {
				System.out.println("���е�"+i+"�αȽϣ�");
				String similarity="";
				Double temp=0.0;
				Process proc;
				try {
					System.out.print("��ǰ�Ƚϵ�Ϊ��"+VectorPath.get(i)+"\t");
					String[] arguments = new String[] {pyInterpreterPath,get_simm,VectorPath.get(i)};
					proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
					//���������������ȡ���
					BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
					String line = null;
					while ((line = in.readLine()) != null) {
					//	System.out.println(line);
						similarity += line;
						System.out.println(similarity);
					}
					in.close();
					proc.waitFor();
				} catch (IOException e) {
					e.printStackTrace();
				} catch (InterruptedException e) {
					e.printStackTrace();
				} 
				
				temp = Double.parseDouble(similarity);
				System.out.println("��ǰ���յ������ƶ�Ϊ��"+temp);
				System.out.println("��ǰ�����ƶ�Ϊ��"+sim);
				if(temp > sim) {
					sim = temp;		
				//�����ʱ��matrix1_username_f1.csv��
					dis_name = all_VName.get(i);
				}
			}
			
			//��ʱdis_name����ӵ��������ƶȵ�matrix1_username_f1.txt�� ���д���
			String[] x = dis_name.split("_");
			System.out.print("�ָ����ַ�Ϊ��");
			for(int i = 0;i<x.length;i++){
			      System.out.print(" " + x[i]);
			 }
			String result = sim+"_"+x[1];
			return result;
					}
		
		public static String distinguish_name(String sim_name) {
			//����õ����ƶȺ�username
			String[] x = sim_name.split("_");
			System.out.print("������ƶȺͶ�ӦusernameΪ:");
			for(int i = 0;i<x.length;i++){
			      System.out.print(" " + x[i]);
			 }
			Double sim = Double.parseDouble(x[0]);
			String name = x[1];
			if(sim>=0.85) {
				return name ;
			}
			else
				return "";
		}
		
		 
}
