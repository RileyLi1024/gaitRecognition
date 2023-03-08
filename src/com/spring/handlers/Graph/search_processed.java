package com.spring.handlers.Graph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class search_processed {
	public static boolean search(String video){
		String path = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Process";
		File file = new File(path);		//获取其file对象
		File[] fs = file.listFiles(); //fs数组里存的都是路径啊
	
		int n = fs.length;
		String filename="";
		for(int i =0;i<n;i++)
		{	
			filename = fs[i].getName();
			if(filename.equals(video)) {
			System.out.println("该视频已经提取过！");
					return false;
					}
		
		}
		System.out.println("该视频需要进行行人提取！");
		return true;
	}
}
