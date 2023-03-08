package com.spring.handlers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.RandomAccessFile;
import java.util.ArrayList;
import java.util.List;

import javax.el.ArrayELResolver;


public class StreamReaderThread implements Runnable {
    /*
     * python的输出流
     */
    private InputStream inputStream;
    /*
     * 输出信息保存的文件名称
     */
    private String logName;

    public StreamReaderThread(InputStream inputStream,String logName){
        this.inputStream = inputStream;
        this.logName = logName;
    }  

	public void run() {
		BufferedReader in = null;
		FileWriter fwriter = null;
		File file = new File("pythondata.txt");
		try {
			in = new BufferedReader(new InputStreamReader(this.inputStream));
			fwriter = new FileWriter(logName, true);
			String line = null;
			while ((line = in.readLine()) != null) {
				fwriter.write(line);
				System.out.println(line);
				FileOutputStream outputStream;
				try {
//					outputStream = new FileOutputStream(file);
					// 打开一个随机访问文件流，按读写方式
					RandomAccessFile randomFile = new RandomAccessFile(file, "rw");
					// 文件长度，字节数
					long fileLength = randomFile.length();
					// 将写文件指针移到文件尾。
					randomFile.seek(fileLength);
					randomFile.writeBytes(line+"\r\n");
					randomFile.close();

//
//					outputStream.write(line.getBytes());
//					outputStream.close();
				} catch (Exception e) {
					e.printStackTrace();
				}
				
			}

		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				inputStream.close();
				fwriter.flush();
				fwriter.close();
				in.close();
			} catch (IOException e) {
				e.printStackTrace();
			}			
		}
	}

}
       
