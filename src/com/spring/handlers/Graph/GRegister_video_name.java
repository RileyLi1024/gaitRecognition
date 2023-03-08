package com.spring.handlers.Graph;

import java.io.*;
import java.util.*;

public class GRegister_video_name {

	public static void save_video_name(String name)throws IOException {
		//保存第一步需要提取的多人视频名
		System.out.println("我要写txt存名字了："+name);
		byte[] sourceByte = name.getBytes();
		
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\video_name.txt";
		File file = new File(path);
		
		FileOutputStream outStream = new FileOutputStream(file);
		outStream.write(sourceByte);
		outStream.close();	
	}
	
	//获取第一步需要提取的多人视频名
	public static String get_track_person()throws IOException {
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\track_person.txt";	
		StringBuilder result = new StringBuilder();
        try{
            BufferedReader br = new BufferedReader(new FileReader(path));//构造一个BufferedReader类来读取文件
            String s = null;
            while((s = br.readLine())!=null){//使用readLine方法，一次读一行
                result.append(System.lineSeparator()+s);
            }
            br.close();    
        }catch(Exception e){
            e.printStackTrace();
        }
        return result.toString();
	}
	
	
	public static void save_tarck_person(String v,int flag)throws IOException {
		//保存待追踪人的信息
		String track_p = "";
	
		if(flag == 1) //第一次保存 保存的是待追踪人的视频名
			{			
				track_p = v+"/";
				System.out.println("保存待追踪人的视频信息："+track_p);
				}
		else if(flag == 2) { //第二次保存 保存的是待追踪人的id
			System.out.println("保存待追踪人的id信息："+v);
			StringBuilder video_path = new StringBuilder();
			//保存第一次存的待追踪人视频名
			String filePath = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\track_person.txt";
	        FileInputStream fin = new FileInputStream(filePath);
	        InputStreamReader reader = new InputStreamReader(fin);
	        BufferedReader buffReader = new BufferedReader(reader);
	        String strTmp = "";
	        while((strTmp = buffReader.readLine())!=null){
	            System.out.println(strTmp);
	            video_path.append(strTmp);
	        }
//	        System.out.println("视频id:"+video_path.toString());
	        buffReader.close();
	        video_path.append(v);
	        track_p = video_path.toString();
	        System.out.println("待追踪人信息："+track_p);
		}
		byte[] sourceByte = track_p.getBytes();
		
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\track_person.txt";
		
		File file = new File(path);
		FileOutputStream outStream = new FileOutputStream(file);
		outStream.write(sourceByte);
		outStream.close();	
	}
}
