package com.spring.handlers;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class NetAndSimilarity {
	//�Լ��Ļ��� ģ���ڵĻ��� ֻ���þ���·��
//	private static final String pyInterpreterPath = "C:\\Users\\ASUS\\Anaconda3\\envs\\zd\\python.exe";
	private static final String pyInterpreterPath = "E:\\Anaconda3\\envs\\pytorch\\python.exe";
	private static final String path = "E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py";

	
	// private static Process proc = null;//java������
	
    public static String compute() {
    	String f = "";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,path};
//			String command="cmd /c&&activate pytorch&&python E:\\workspace-sts\\Gait\\cnn+lstm\\get_sim.py ";
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			System.out.println("python����������ƶ�");
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
				f +=line;
				System.out.println("���ƶ�Ϊf��"+f);
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

	
	public static void main(String[] args) {

	}

}

