package com.spring.handlers.Graph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class search_registervideo {

	public static List<String> search_rv(){
		String path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register";
		File file = new File(path);		//��ȡ��file����
		File[] fs = file.listFiles(); //fs�������Ķ���·����
		List<String> vname = new ArrayList<String>();
		int n = fs.length;
		//String[] id = new String[n];
		String filename;
	//	System.out.println("����IDΪ��");
		for(int i =0;i<n;i++)
		{	
			filename = fs[i].getName();//��·���õ��ļ���	
			vname.add(filename);
		
		}
		System.out.println("��ǰע�������ƵΪ��");
		for(int i =0;i<vname.size();i++) {
			System.out.println(vname.get(i));}
		return vname;
	}
}
