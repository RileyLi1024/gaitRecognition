package com.spring.handlers;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class empty_folder {
	private static final String pyInterpreterPath = "python";
	private static final String empty = "E:\\workspace-sts\\Gait\\Matrix_Python\\empty.py";
	
	 public static void empty() {
	    	Process proc;
			try {
				
				System.out.println("����empty()");
				String[] arguments = new String[] {pyInterpreterPath,empty};
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
		
		public static void main() {
			// TODO Auto-generated method stub
			System.out.println("��մ����ļ��У�");
			empty();
		
		}

	
}
