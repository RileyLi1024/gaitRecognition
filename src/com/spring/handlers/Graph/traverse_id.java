package com.spring.handlers.Graph;
import java.io.*;

public class traverse_id {
	public static int traverse(String id) {
		
		//读取当前视频名
		String video_name = get_rname();
		
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register\\"+video_name+"\\";
	   
	    //找是否已注册过（即path文件夹下有没有id文件夹）	    
	    int flag = func(path,id);
		//int flag = 1;
		//search(path,id_video);
		return flag;
	}
	
	public static String get_rname() {
		String video_name_path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\video_name.txt";
		String video_name = "";
		try (FileReader reader = new FileReader(video_name_path);
	             BufferedReader br = new BufferedReader(reader) // 建立一个对象，它把文件内容转成计算机能读懂的语言
	        ) {
	            String line;
	            //网友推荐更加简洁的写法
	            while ((line = br.readLine()) != null) {
	                // 一次读入一行数据
	            	video_name = line.replace(".mp4", "");
	                System.out.println("当前注册视频为："+video_name);
	            }
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
		return video_name;
	} 
	
	
	public static int func(String path,String id) {
		
			File f = new File(path); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  String id_name = file.getName();
			  System.out.println("寻找中...");
			  if (file.isDirectory() && id_name.equals(id) ) 
			  { 
				  System.out.println("找到了注册视频"+f.getName()+"文件夹中已注册的ID:"+id_name);
				  return 0 ;
			   }
			 } 
			}
			System.out.println("没找到，尚未注册！");
			return 1;		
	}

}
