package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;



public class javaInvokeTrack {

	//�Լ��Ļ��� ģ���ڵĻ��� ֻ���þ���·��
//	��openh264-1.8.0-win64.dll�ŵ�python.exe�ĸ�Ŀ¼��E:\\Anaconda3\\envs\\shihy
	
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\shihy\\python.exe";
	
	private static final String path = "E:\\workspace-sts\\Gait\\GaitGraph-main\\src\\evaluatenew1.py";	
	// private static Process proc = null;//java������
	
    public static ArrayList<String> Track() {
    	ArrayList<String> result_path = new ArrayList<String>();
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path};
//			String[] arguments = initParams();
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			System.out.println("python���봦����Ƶ��");
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {			
				result_path.add(line);
				//System.out.println("�жϽ��Ϊ��"+f);
			}
			in.close();
			for(int i=0;i<result_path.size();i++) {
				System.out.println("result_path:"+result_path.get(i));
			}
//			proc.waitFor();
			System.out.println("python�ɹ��ҵ�����������Ƶ��");
		} catch (IOException e) {
			e.printStackTrace();
		}
//		catch (InterruptedException e) {
//			e.printStackTrace();
//		}
		
		return result_path;
    }


	
}
