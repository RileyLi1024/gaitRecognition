package com.spring.handlers.Graph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class search_id {
	public static List<String> search(int type,String video) {
		//ע�� ����Process�����ɵ�����id
		String t = "";
		
		if(type == 1) t = "Process";
	else if(type == 2) t = "Register";
	else if(type == 3) t = "result_all";
		List<String> id = new ArrayList<String>();
		
		String path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\"+t+"\\"+video+"\\";
		File file = new File(path);		//��ȡ��file����
		File[] fs = file.listFiles(); //fs�������Ķ���·����
	
		int n = fs.length;
		//String[] id = new String[n];
		String filename;
	//	System.out.println("����IDΪ��");
		for(int i =0;i<n;i++)
		{	
			filename = fs[i].getName();//��·���õ��ļ���	
			if(!(filename.endsWith(".mp4"))) {
				id.add(filename);
				}
		
		}
		System.out.println("����IDΪ��");
		for(int i =0;i<id.size();i++) {
			System.out.println(id.get(i));}
		
		return id;
	}
}
