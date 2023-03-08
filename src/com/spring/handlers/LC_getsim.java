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
		//找到所有注册用户视频的特征向量
		List<String> all_VectorName = new ArrayList<String>();
		all_VectorName=search("E:\\workspace-sts\\Gait\\Register");
		//依次调用余弦相似度度量py脚本进行比对 返回的是“double最高相似度，对应的username”
		String sim_name = get_Sim(all_VectorName);
		String result =distinguish_name(sim_name);
		return result;
		}
			 
		public static List<String> search(String path)
		{
		System.out.println("遍历注册列表：");
		   File dir = new File(path);		 
		   List<String> all_VName = new ArrayList<String>(); //保存所有注册视频特征向量的名字
		   //不找子目录
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
				System.out.print("遍历向量名列表："+all_VName.get(i) );
				VectorPath.add("E:\\workspace-sts\\Gait\\Register\\"+all_VName.get(i));
			}
			
			for (int j = 0; j < VectorPath.size(); j++) {
				System.out.print("遍历向量路径列表："+VectorPath.get(j)+"\t");
			}
			
			//依次调用py脚本得到相似度结果 这里有问题了哈哈哈  存成matrix_username_f1.csv 大不了每个都比
			//不用很麻烦的一个Usrname一个相似度结果表 直接找到最大的然后getname然后_作为分割线 分割出username就是判别结果~~~
			Double sim = 0.0;
			String dis_name ="";
			System.out.println("已经注册的用户数量为："+VectorPath.size());
			for (int i = 0;i<VectorPath.size(); i++) {
				System.out.println("进行第"+i+"次比较！");
				String similarity="";
				Double temp=0.0;
				Process proc;
				try {
					System.out.print("当前比较的为："+VectorPath.get(i)+"\t");
					String[] arguments = new String[] {pyInterpreterPath,get_simm,VectorPath.get(i)};
					proc = Runtime.getRuntime().exec(arguments);// 执行py文件
					//用输入输出流来截取结果
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
				System.out.println("当前接收到的相似度为："+temp);
				System.out.println("当前的相似度为："+sim);
				if(temp > sim) {
					sim = temp;		
				//保存此时的matrix1_username_f1.csv名
					dis_name = all_VName.get(i);
				}
			}
			
			//此时dis_name里是拥有最大相似度的matrix1_username_f1.txt名 进行处理
			String[] x = dis_name.split("_");
			System.out.print("分割后的字符为：");
			for(int i = 0;i<x.length;i++){
			      System.out.print(" " + x[i]);
			 }
			String result = sim+"_"+x[1];
			return result;
					}
		
		public static String distinguish_name(String sim_name) {
			//处理得到相似度和username
			String[] x = sim_name.split("_");
			System.out.print("最高相似度和对应username为:");
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
