package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;



public class javaInvokeTrack {

	//自己的环境 模型在的环境 只能用绝对路径
//	将openh264-1.8.0-win64.dll放到python.exe的根目录下E:\\Anaconda3\\envs\\shihy
	
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\shihy\\python.exe";
	
	private static final String path = "E:\\workspace-sts\\Gait\\GaitGraph-main\\src\\evaluatenew1.py";	
	// private static Process proc = null;//java进程类
	
    public static ArrayList<String> Track() {
    	ArrayList<String> result_path = new ArrayList<String>();
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path};
//			String[] arguments = initParams();
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
			System.out.println("python进入处理视频！");
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {			
				result_path.add(line);
				//System.out.println("判断结果为："+f);
			}
			in.close();
			for(int i=0;i<result_path.size();i++) {
				System.out.println("result_path:"+result_path.get(i));
			}
//			proc.waitFor();
			System.out.println("python成功找到相似行人视频！");
		} catch (IOException e) {
			e.printStackTrace();
		}
//		catch (InterruptedException e) {
//			e.printStackTrace();
//		}
		
		return result_path;
    }


	
}
