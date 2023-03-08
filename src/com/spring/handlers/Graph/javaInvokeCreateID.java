package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class javaInvokeCreateID {

	//自己的环境 模型在的环境 只能用绝对路径

	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\shihy\\python.exe";
	private static final String path = "E:\\workspace-sts\\Gait\\GaitGraph-main\\detectandsave\\secondstep.py";	
	// private static Process proc = null;//java进程类
	
    public static void create_id_video(String id) {
    	
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path,id};
//			String command="cmd /c&&activate pytorch&&python E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py ";
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
			System.out.println("python进入处理视频！");
			proc.waitFor();
			System.out.println("python成功生成注册ID视频！");
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		
    }


	
}
