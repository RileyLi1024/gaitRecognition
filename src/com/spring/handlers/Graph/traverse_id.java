package com.spring.handlers.Graph;
import java.io.*;

public class traverse_id {
	public static int traverse(String id) {
		
		//��ȡ��ǰ��Ƶ��
		String video_name = get_rname();
		
		String path="E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register\\"+video_name+"\\";
	   
	    //���Ƿ���ע�������path�ļ�������û��id�ļ��У�	    
	    int flag = func(path,id);
		//int flag = 1;
		//search(path,id_video);
		return flag;
	}
	
	public static String get_rname() {
		String video_name_path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\video_name.txt";
		String video_name = "";
		try (FileReader reader = new FileReader(video_name_path);
	             BufferedReader br = new BufferedReader(reader) // ����һ�����������ļ�����ת�ɼ�����ܶ���������
	        ) {
	            String line;
	            //�����Ƽ����Ӽ���д��
	            while ((line = br.readLine()) != null) {
	                // һ�ζ���һ������
	            	video_name = line.replace(".mp4", "");
	                System.out.println("��ǰע����ƵΪ��"+video_name);
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
			  System.out.println("Ѱ����...");
			  if (file.isDirectory() && id_name.equals(id) ) 
			  { 
				  System.out.println("�ҵ���ע����Ƶ"+f.getName()+"�ļ�������ע���ID:"+id_name);
				  return 0 ;
			   }
			 } 
			}
			System.out.println("û�ҵ�����δע�ᣡ");
			return 1;		
	}

}
