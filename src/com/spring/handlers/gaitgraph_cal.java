package com.spring.handlers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class gaitgraph_cal {
	
	private static final String pyInterpreterPath = "python";
	private static final String matrix_graph = "E:\\workspace-sts\\Gait\\Matrix_Python\\Matrix_graph.py";
	
    public static void cal_GraphMatrix() {
    	String number="";
    	Process proc;
		try {
			
			String[] arguments = new String[] {pyInterpreterPath,matrix_graph};
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
		System.out.println("开始计算计算图卷积网络矩阵");
		cal_GraphMatrix();
	//	rename(path_p2);
	}

}
