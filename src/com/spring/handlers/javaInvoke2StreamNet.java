package com.spring.handlers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class javaInvoke2StreamNet {
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\pytorch\\python.exe";
	private static final String path = "E:\\workspace-sts\\Gait\\two_streanm_net_resnet50_newdata\\main.py";

	
	// private static Process proc = null;//java������
	
    public static String compute() {
    	String f = "";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path};
//			String command="cmd /c&&activate pytorch&&python E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py ";
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			System.out.println("python����˫������");
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
				f +=line;
				System.out.println("�жϽ��Ϊ��"+f);
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
