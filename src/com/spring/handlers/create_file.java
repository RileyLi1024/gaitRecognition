package com.spring.handlers;
import java.io.*;
public class create_file {
	@SuppressWarnings("resource")
	public static int create(String username,String name)throws IOException {
		//获取要复制的文件
    	File oldfile1=new File("E:\\workspace-sts\\Gait\\Matrix\\video2\\real_one.csv");
    	File oldfile2=new File("E:\\workspace-sts\\Gait\\Matrix\\video2\\real_two.csv");
    	//文件输入流，用于读取要复制的文件
    	FileInputStream fileInputStream1 = new FileInputStream(oldfile1);
    	FileInputStream fileInputStream2 = new FileInputStream(oldfile2);
    	
    	//获取视频名，截掉后缀.mp4
        //截掉字符串后5位
        String subname = name.substring(0,name.length()-4);
		
    	//要生成的新文件（指定路径如果没有则创建）
    	String path = "E:\\workspace-sts\\Gait\\Register\\"+username+"\\"+subname;
    	System.out.println(path);
        //具体到文件，因为不可能访问一个空文件夹 要一个载体才能输出
    	File newfile1=new File(path+"\\real_one.csv");
    	File newfile2=new File(path+"\\real_two.csv");
    	if (!newfile1.getParentFile().exists()) {
    		newfile1.getParentFile().mkdirs();
    		System.out.println("创建目录成功");
    	}
    	else
    	{
    		System.out.println("该视频已注册！");
    		return 1;
    	}
    	//其实没必要 因为在都在一个路径下
//    	if (!newfile2.getParentFile().exists()) {
//    		newfile2.getParentFile().mkdirs();
//    		System.out.println("创建2成功");
//    	}
    	
    	//新文件输出流
    	FileOutputStream fileOutputStream1 = new FileOutputStream (newfile1);
    	FileOutputStream fileOutputStream2 = new FileOutputStream (newfile2);
    	byte[] buffer1= new byte[1024];
    	int len1;
    	//将文件流信息读取文件缓存区，如果读取结果不为-1就代表文件没有读取完毕，反之已经读取完毕
    	while ((len1=fileInputStream1.read(buffer1))!=-1) {
    	fileOutputStream1.write(buffer1, 0, len1);
    	fileOutputStream1.flush();
    	}
    	fileInputStream1.close();
    	fileOutputStream1.close();   
    	
    	byte[] buffer2= new byte[1024];
    	int len2;
    	//将文件流信息读取文件缓存区，如果读取结果不为-1就代表文件没有读取完毕，反之已经读取完毕
    	while ((len2=fileInputStream2.read(buffer2))!=-1) {
    	fileOutputStream2.write(buffer2, 0, len2);
    	fileOutputStream2.flush();
    	}
    	fileInputStream2.close();    	
    	fileOutputStream2.close();
    	
    	//将该文件夹里的特征向量送入网络得到特征向量 输出到path路径的matrix1.csv中
    	
    	
    	return 0;
    }
    
		
	
	
    public static void main(){
    	   
    }
    
    
}