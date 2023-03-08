package com.spring.handlers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class rename_p {
	
	private static final String pyInterpreterPath = "python";
	private static final String rename_p = "E:\\workspace-sts\\Gait\\Matrix_Python\\rename_p.py";
//	private static final String path_p1 = "E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video1";
//	private static final String path_p2 = "E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video2";
	
    public static void rename() {
    	String number="";
    	Process proc;
		try {
			
			String[] arguments = new String[] {pyInterpreterPath,rename_p};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
				number += line;
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		System.out.println(number);
    	
    }
	
	public static void main() {
		// TODO Auto-generated method stub
		System.out.println("进入rename");
		rename();
	//	rename(path_p2);
	}

}
