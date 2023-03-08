package com.spring.handlers.Graph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class search_registervideo {

	public static List<String> search_rv(){
		String path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register";
		File file = new File(path);		//获取其file对象
		File[] fs = file.listFiles(); //fs数组里存的都是路径啊
		List<String> vname = new ArrayList<String>();
		int n = fs.length;
		//String[] id = new String[n];
		String filename;
	//	System.out.println("现有ID为：");
		for(int i =0;i<n;i++)
		{	
			filename = fs[i].getName();//从路径得到文件名	
			vname.add(filename);
		
		}
		System.out.println("当前注册过的视频为：");
		for(int i =0;i<vname.size();i++) {
			System.out.println(vname.get(i));}
		return vname;
	}
}
