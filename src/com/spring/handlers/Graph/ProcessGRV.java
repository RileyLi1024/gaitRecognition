package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ProcessGRV {

	//�Լ��Ļ��� ģ���ڵĻ��� ֻ���þ���·��
		private static final String pyInterpreterPath = "C:\\Users\\ASUS\\Anaconda3\\envs\\zd\\python.exe";
		private static final String path = "G:\\Wy\\cnn+lstm\\get_sim.py";

		

		
	    public static void compute_matrix(String username,String name) {
	    	System.out.println("����LC������õ�����������");
	    	Process proc;
			try {
				String[] arguments = new String[] {pyInterpreterPath,path,username,name};
				proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
				//���������������ȡ���
				BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
				String line = null;
				while ((line = in.readLine()) != null) {
					System.out.println(line);

				}
				in.close();
				proc.waitFor();
			} catch (IOException e) {
				e.printStackTrace();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
	    }
	
}
