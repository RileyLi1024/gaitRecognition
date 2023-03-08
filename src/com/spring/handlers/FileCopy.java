package com.spring.handlers;
import java.io.*;

import org.apache.commons.compress.utils.IOUtils;
public class FileCopy {
    public static void main(String[] args){
        File sourceFile = new File("E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output\\video");
        File targetFile = new File("E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1");// Ŀ���ļ�
        String target = "E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1";
      //  deleteDir(target);
//        FileOutputStream fout = new FileOutputStream(targetFile);
        
//        if(targetFile.exists()) 
//        { 
//        	targetFile.delete();
//        }
//        targetFile.createNewFile();
        
        copyDirectory(sourceFile, targetFile);
    }
    public static void copyDirectory(File sourceFile, File targetFile) {
        if (sourceFile.isFile()) {// ������ļ�,��ֱ�Ӹ���
            copyFile(sourceFile, new File(targetFile, sourceFile.getName()));
          
        } else {//�����Ŀ¼,�����
            File file = new File(targetFile, sourceFile.getName());//�������ļ���
            file.mkdirs();
       
            File[] files = sourceFile.listFiles();
            for (File file2 : files) {
                copyDirectory(file2, file);
            }
        }
    }

    public static void copyFile(File sourceFile, File targetFile) {
        BufferedInputStream bis = null;
        BufferedOutputStream bos = null;
        try {
            bis = new BufferedInputStream(new FileInputStream(sourceFile));
            bos = new BufferedOutputStream(new FileOutputStream(targetFile));
            byte[] buff = new byte[1024];
            int length;
            while (-1 != (length = bis.read(buff))) {
                bos.write(buff, 0, length);
            }
            bos.flush();
        } catch (FileNotFoundException e) {
            System.out.println("·��������");
            System.exit(-1);
        } catch (IOException e) {
            System.out.println("�ļ���д����");
            System.exit(-1);
        } finally {
            IOUtils.closeQuietly(bis);
            IOUtils.closeQuietly(bos);
        }
    }
    

    
    
    
}


