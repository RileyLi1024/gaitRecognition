package com.spring.handlers.Graph;
import java.io.*;
public class create_file {
	public static void create(String v) {
		// 保存第一步多人视频名
		String path1 = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register";
		//删除.mp4后缀
		String video_name = v.replace(".mp4", "");
		
		String path2 = path1+"\\"+video_name;
		//生成文件夹
		File file=new File(path2);
		if(!file.exists()){	//如果_test2文件夹不存在
		    file.mkdir();		//创建文件夹
		}
	}
	
	public static void person_video(String v) {
		// 保存第一步多人视频名
		String path1 = "E:\\workspace-sts\\Gait\\WebContent\\Graph\\Register";
		//删除.mp4后缀
		String video_name = v.replace(".mp4", "");
		
		String path2 = path1+"\\"+video_name;
		//生成文件夹
		File file=new File(path2);
		if(!file.exists()){	//如果_test2文件夹不存在
		    file.mkdir();		//创建文件夹
		}
	}
}
