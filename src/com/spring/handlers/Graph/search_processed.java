package com.spring.handlers.Graph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class search_processed {
	public static boolean search(String video){
		String path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Process";
		File file = new File(path);		//��ȡ��file����
		File[] fs = file.listFiles(); //fs�������Ķ���·����
	
		int n = fs.length;
		String filename="";
		for(int i =0;i<n;i++)
		{	
			filename = fs[i].getName();
			if(filename.equals(video)) {
			System.out.println("����Ƶ�Ѿ���ȡ����");
					return false;
					}
		
		}
		System.out.println("����Ƶ��Ҫ����������ȡ��");
		return true;
	}
}
