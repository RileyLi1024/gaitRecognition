package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class javaInvokeCreateID {

	//�Լ��Ļ��� ģ���ڵĻ��� ֻ���þ���·��

	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\shihy\\python.exe";
	private static final String path = "E:\\workspace-sts\\Gait\\GaitGraph-main\\detectandsave\\secondstep.py";	
	// private static Process proc = null;//java������
	
    public static void create_id_video(String id) {
    	
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path,id};
//			String command="cmd /c&&activate pytorch&&python E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py ";
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			System.out.println("python���봦����Ƶ��");
			proc.waitFor();
			System.out.println("python�ɹ�����ע��ID��Ƶ��");
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		
    }


	
}
