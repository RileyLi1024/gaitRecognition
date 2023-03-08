package com.spring.handlers.Graph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class search_id {
	public static List<String> search(int type,String video) {
		//注册 就在Process找生成的所有id
		String t = "";
		
		if(type == 1) t = "Process";
	else if(type == 2) t = "Register";
	else if(type == 3) t = "result_all";
		List<String> id = new ArrayList<String>();
		
		String path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\"+t+"\\"+video+"\\";
		File file = new File(path);		//获取其file对象
		File[] fs = file.listFiles(); //fs数组里存的都是路径啊
	
		int n = fs.length;
		//String[] id = new String[n];
		String filename;
	//	System.out.println("现有ID为：");
		for(int i =0;i<n;i++)
		{	
			filename = fs[i].getName();//从路径得到文件名	
			if(!(filename.endsWith(".mp4"))) {
				id.add(filename);
				}
		
		}
		System.out.println("现有ID为：");
		for(int i =0;i<id.size();i++) {
			System.out.println(id.get(i));}
		
		return id;
	}
}
