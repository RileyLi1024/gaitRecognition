package com.spring.handlers.Graph;
import java.io.*;
public class create_file {
	public static void create(String v) {
		// �����һ��������Ƶ��
		String path1 = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register";
		//ɾ��.mp4��׺
		String video_name = v.replace(".mp4", "");
		
		String path2 = path1+"\\"+video_name;
		//�����ļ���
		File file=new File(path2);
		if(!file.exists()){	//���_test2�ļ��в�����
		    file.mkdir();		//�����ļ���
		}
	}
	
	public static void person_video(String v) {
		// �����һ��������Ƶ��
		String path1 = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register";
		//ɾ��.mp4��׺
		String video_name = v.replace(".mp4", "");
		
		String path2 = path1+"\\"+video_name;
		//�����ļ���
		File file=new File(path2);
		if(!file.exists()){	//���_test2�ļ��в�����
		    file.mkdir();		//�����ļ���
		}
	}
}
