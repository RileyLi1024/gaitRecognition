package com.spring.handlers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class javaInvokeGaitGraph {
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\GaitGraph\\python.exe";
	private static final String path = "E:\\workspace-sts\\Gait\\GaitGraph-main\\src\\evaluatenew.py";

	
	// private static Process proc = null;//java进程类
	
    public static String compute() {
    	String f = "";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path};
//			String command="cmd /c&&activate pytorch&&python E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py ";
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
			System.out.println("python进入图卷积网络");
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
				f +=line;
				System.out.println("判断结果为："+f);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		return f;
    }

	
}
