package com.spring.handlers.Graph;

import java.io.*;
import java.util.*;

public class GRegister_video_name {

	public static void save_video_name(String name)throws IOException {
		//�����һ����Ҫ��ȡ�Ķ�����Ƶ��
		System.out.println("��Ҫдtxt�������ˣ�"+name);
		byte[] sourceByte = name.getBytes();
		
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\video_name.txt";
		File file = new File(path);
		
		FileOutputStream outStream = new FileOutputStream(file);
		outStream.write(sourceByte);
		outStream.close();	
	}
	
	//��ȡ��һ����Ҫ��ȡ�Ķ�����Ƶ��
	public static String get_track_person()throws IOException {
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\track_person.txt";	
		StringBuilder result = new StringBuilder();
        try{
            BufferedReader br = new BufferedReader(new FileReader(path));//����һ��BufferedReader������ȡ�ļ�
            String s = null;
            while((s = br.readLine())!=null){//ʹ��readLine������һ�ζ�һ��
                result.append(System.lineSeparator()+s);
            }
            br.close();    
        }catch(Exception e){
            e.printStackTrace();
        }
        return result.toString();
	}
	
	
	public static void save_tarck_person(String v,int flag)throws IOException {
		//�����׷���˵���Ϣ
		String track_p = "";
	
		if(flag == 1) //��һ�α��� ������Ǵ�׷���˵���Ƶ��
			{			
				track_p = v+"/";
				System.out.println("�����׷���˵���Ƶ��Ϣ��"+track_p);
				}
		else if(flag == 2) { //�ڶ��α��� ������Ǵ�׷���˵�id
			System.out.println("�����׷���˵�id��Ϣ��"+v);
			StringBuilder video_path = new StringBuilder();
			//�����һ�δ�Ĵ�׷������Ƶ��
			String filePath = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\track_person.txt";
	        FileInputStream fin = new FileInputStream(filePath);
	        InputStreamReader reader = new InputStreamReader(fin);
	        BufferedReader buffReader = new BufferedReader(reader);
	        String strTmp = "";
	        while((strTmp = buffReader.readLine())!=null){
	            System.out.println(strTmp);
	            video_path.append(strTmp);
	        }
//	        System.out.println("��Ƶid:"+video_path.toString());
	        buffReader.close();
	        video_path.append(v);
	        track_p = video_path.toString();
	        System.out.println("��׷������Ϣ��"+track_p);
		}
		byte[] sourceByte = track_p.getBytes();
		
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\track_person.txt";
		
		File file = new File(path);
		FileOutputStream outStream = new FileOutputStream(file);
		outStream.write(sourceByte);
		outStream.close();	
	}
}
