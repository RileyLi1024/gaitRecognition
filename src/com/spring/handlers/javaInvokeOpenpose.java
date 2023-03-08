package com.spring.handlers;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;




public class javaInvokeOpenpose {
	
	private static Process proc = null;//java进程类
	
	 public static void execPy(String firstperson,String type) {   	
	        try {
	        	
	        	System.out.println("进入Openpose");
	        	String runpath="E:\\workspace-sts\\Gait\\WebContent\\video\\";
	        	firstperson=runpath+firstperson;
	        	String command="cmd /c E:&&cd E:\\workspace-sts\\Gait\\Pose3Dkeypoints&&activate openpose&&python E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\run.py "+firstperson+" "+type;
//	        	String command="cmd /k dir";
	        	System.out.println("视频："+firstperson);
	        	proc = Runtime.getRuntime().exec(command);
	            BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
	            Thread thread1 = new Thread(new StreamReaderThread(proc.getInputStream(),"normal.txt"));
	            Thread thread2 = new Thread(new StreamReaderThread(proc.getErrorStream(),"error.txt"));
	            thread2.start();
	            thread1.start();//必须后执行，否则正确消息容易接收不到
	            int re = proc.waitFor();//返回0：成功。其余返回值均表示失败，如：返回错误代码1：操作不允许，表示调用python脚本失败
	            System.out.println(re);
	            Thread.sleep(1000);//等待后台线程读写完毕
	            System.out.println("python program done!!!"); 
	           
	        } catch (IOException e) {
	            e.printStackTrace();
	        } catch (InterruptedException e) {
	            e.printStackTrace();
	        }

	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 String fp = "";
		 String type="v";
        execPy(fp,type);
	}

}
