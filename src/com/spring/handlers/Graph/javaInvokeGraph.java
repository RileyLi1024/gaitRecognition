package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class javaInvokeGraph {

	//�Լ��Ļ��� ģ���ڵĻ��� ֻ���þ���·��

	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\shihy\\python.exe";
	private static final String path = "E:\\workspace-sts\\Gait\\GaitGraph-main\\detectandsave\\firststep.py";

	
	// private static Process proc = null;//java������
	
    public static void extract() {
    	
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path};
//			String command="cmd /c&&activate pytorch&&python E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py ";
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			System.out.println("python���봦����Ƶ��");
			//BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			//String line = null;
//			while ((line = in.readLine()) != null) {
//				System.out.println("�������Ķ���"+line);
//				
//			}
			//in.close();
			proc.waitFor();
			System.out.println("python��ȡ������ɣ�");
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		
    }


	
}
