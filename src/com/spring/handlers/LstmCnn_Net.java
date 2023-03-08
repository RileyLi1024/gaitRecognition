package com.spring.handlers;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class LstmCnn_Net {
	//�Լ��Ļ��� ģ���ڵĻ��� ֻ���þ���·��
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\pytorch\\python.exe";
	private static final String get_feature = "E:\\workspace-sts\\Gait\\cnn+lstm\\get_feature.py";

	

	
    public static void compute_matrix(String username,String name) {
    	System.out.println("����LC������õ�����������");
    	String result = "";
    	Process proc;
    	String subname = name.substring(0,name.length()-4);
		try {
//			String path1 = "E:\\workspace-sts\\Gait\\Register\\"+username+"\\"+subname+"\\real_one.csv";
//			String path2 = "E:\\workspace-sts\\Gait\\Register\\"+username+"\\"+subname+"\\real_two.csv";	
			String[] arguments = new String[] {pyInterpreterPath,get_feature,username,subname};		
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				//System.out.println(line);
				result += line;
			}
			System.out.println("�����"+result);
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

    }

	public static void main(String[] args) {

	}

}

