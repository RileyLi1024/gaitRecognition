package com.spring.handlers;
import java.io.*;
public class create_file {
	@SuppressWarnings("resource")
	public static int create(String username,String name)throws IOException {
		//��ȡҪ���Ƶ��ļ�
    	File oldfile1=new File("E:\\workspace-sts\\Gait\\Matrix\\video2\\real_one.csv");
    	File oldfile2=new File("E:\\workspace-sts\\Gait\\Matrix\\video2\\real_two.csv");
    	//�ļ������������ڶ�ȡҪ���Ƶ��ļ�
    	FileInputStream fileInputStream1 = new FileInputStream(oldfile1);
    	FileInputStream fileInputStream2 = new FileInputStream(oldfile2);
    	
    	//��ȡ��Ƶ�����ص���׺.mp4
        //�ص��ַ�����5λ
        String subname = name.substring(0,name.length()-4);
		
    	//Ҫ���ɵ����ļ���ָ��·�����û���򴴽���
    	String path = "E:\\workspace-sts\\Gait\\Register\\"+username+"\\"+subname;
    	System.out.println(path);
        //���嵽�ļ�����Ϊ�����ܷ���һ�����ļ��� Ҫһ������������
    	File newfile1=new File(path+"\\real_one.csv");
    	File newfile2=new File(path+"\\real_two.csv");
    	if (!newfile1.getParentFile().exists()) {
    		newfile1.getParentFile().mkdirs();
    		System.out.println("����Ŀ¼�ɹ�");
    	}
    	else
    	{
    		System.out.println("����Ƶ��ע�ᣡ");
    		return 1;
    	}
    	//��ʵû��Ҫ ��Ϊ�ڶ���һ��·����
//    	if (!newfile2.getParentFile().exists()) {
//    		newfile2.getParentFile().mkdirs();
//    		System.out.println("����2�ɹ�");
//    	}
    	
    	//���ļ������
    	FileOutputStream fileOutputStream1 = new FileOutputStream (newfile1);
    	FileOutputStream fileOutputStream2 = new FileOutputStream (newfile2);
    	byte[] buffer1= new byte[1024];
    	int len1;
    	//���ļ�����Ϣ��ȡ�ļ��������������ȡ�����Ϊ-1�ʹ����ļ�û�ж�ȡ��ϣ���֮�Ѿ���ȡ���
    	while ((len1=fileInputStream1.read(buffer1))!=-1) {
    	fileOutputStream1.write(buffer1, 0, len1);
    	fileOutputStream1.flush();
    	}
    	fileInputStream1.close();
    	fileOutputStream1.close();   
    	
    	byte[] buffer2= new byte[1024];
    	int len2;
    	//���ļ�����Ϣ��ȡ�ļ��������������ȡ�����Ϊ-1�ʹ����ļ�û�ж�ȡ��ϣ���֮�Ѿ���ȡ���
    	while ((len2=fileInputStream2.read(buffer2))!=-1) {
    	fileOutputStream2.write(buffer2, 0, len2);
    	fileOutputStream2.flush();
    	}
    	fileInputStream2.close();    	
    	fileOutputStream2.close();
    	
    	//�����ļ����������������������õ��������� �����path·����matrix1.csv��
    	
    	
    	return 0;
    }
    
		
	
	
    public static void main(){
    	   
    }
    
    
}