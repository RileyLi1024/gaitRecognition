package com.spring.handlers.Graph;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.apache.catalina.Session;
import org.apache.catalina.startup.HomesUserDatabase;
import org.apache.poi.openxml4j.exceptions.InvalidFormatException;
import org.apache.xmlbeans.impl.xb.xsdschema.Public;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

//import com.models.JointData;
import com.sun.net.httpserver.Authenticator.Success;
import java.io.*;

@Controller


public class Graphgait {
	//注册
	@RequestMapping("/GraphRegister")
	public String showGR() {
		System.out.println("register页面！");
		return "Graphnew/Register/Register";
	}
	
	@RequestMapping("/videoReading")
	public ModelAndView video(HttpServletRequest request) throws IOException {
		System.out.println("videoReading页面！");
		ModelAndView mView = new ModelAndView();
		String realpath = request.getParameter("f1");
		
		String flag ="h";
		int a = realpath.indexOf(flag);
		String video_name = realpath.substring(a+2);

		System.out.println("注册视频名："+video_name);
		//保存注册视频名 并建立一个注册视频名文件夹
		GRegister_video_name.save_video_name(video_name);
		create_file.create(video_name);
		
		mView.addObject("video", video_name);
		mView.setViewName("Graphnew/Register/videoReading");

		return mView;
	}

	/*
	 * @RequestMapping("/searchId") public String[] searchId() { String[] id_name =
	 * null; id_name = search_id.search(); System.out.println("现有ID为："); for(int i =
	 * 0;i<id_name.length;i++) { System.out.println(id_name[i]); } return id_name; }
	 */
	
	
	@RequestMapping("/select")
	public ModelAndView select(){
		//当前注册视频名
		String video = traverse_id.get_rname();
		System.out.println("注册提取好的视频名为："+video);
		//调py处理当前视频 并保存到相应视频名文件夹下 得到处理后的视频名
		//看视频是否处理过
		boolean n = search_processed.search(video);
		if(n)
			{javaInvokeGraph.extract();}
		//处理后视频名
		String register_vname = "Extracted"+video+".mp4";
		System.out.println("提取好的视频名为："+register_vname);	
		List<String> id_name = new ArrayList<String>();
		id_name = search_id.search(1,video);		
		ModelAndView mView = new ModelAndView();
		mView.addObject("video", video);
		mView.addObject("register_vname", register_vname);
		mView.addObject("id_name", id_name);
		mView.setViewName("Graphnew/Register/selectID");
		return mView;
	}
	
	
	
	@RequestMapping("/RegisterID")
	public ModelAndView RegisterID(HttpServletRequest request) throws IOException{
		
		//得到选择的注册ID 连py将对应ID的视频保存到上面建的那个注册视频名文件夹下
		String id = request.getParameter("id");
		System.out.println("现在选择注册的ID："+id);
		// 判断是否重复注册 检索register文件夹 看是否当前注册video_name文件夹下 有现在选择的id文件
		String result = "";
		int flag ;
		flag = traverse_id.traverse(id);
		
		System.out.println("flag="+flag);
		if(flag == 1) {
			javaInvokeCreateID.create_id_video(id);
			result = "注册成功！";
		}
		else if(flag == 0) result = "此id已注册！";
					
		
		ModelAndView mView = new ModelAndView();
		mView.addObject("result", result);
		mView.setViewName("Graphnew/Register/Rresult");
		return mView;
	
	}
	
	@RequestMapping("/test")
	public String showG() {
		System.out.println("testvideo页面！");
		return "Graphnew/testvideo";
	}
	
	
	
	
	//嫌疑人追踪
	@RequestMapping("/GraphTrack")
	public String showGD() {
		System.out.println("Track页面！");
		return "Graphnew/Track/Track";
	}
	
	
	@RequestMapping("/TSelectvideo")
	public ModelAndView TVideo(HttpServletRequest request) throws IOException {
		System.out.println("放上提取好的视频 以及选择注册库中的ID框");
		//当前注册视频名
		String f1 = request.getParameter("f1");
		
		String flag ="h";
		int a = f1.indexOf(flag);
		String video_name = f1.substring(a+2);

		System.out.println("输入待追踪视频名："+video_name);
		//保存待追踪视频名到video_name.txt  video_name.txt永远保存最新提取的视频名
		GRegister_video_name.save_video_name(video_name);
		//调py处理当前视频 并保存到相应视频名文件夹下 得到处理后的视频名
		//看视频是否处理过
		String video = video_name.replace(".mp4", "");
		if(search_processed.search(video))
			{javaInvokeGraph.extract();}
		//处理后视频名
		String track_vname = "Extracted"+video+".mp4";
		System.out.println("提取好的视频名为："+track_vname);			
		//当前注册视频
		List<String> vname = search_registervideo.search_rv();
		
		ModelAndView mView = new ModelAndView();
		mView.addObject("video", video);
		mView.addObject("track_vname", track_vname);
		mView.addObject("vname",vname);	
		mView.setViewName("Graphnew/Track/TSelectvideo");
		return mView;
	}
	
	@RequestMapping("/TSelectid")
	public ModelAndView Tid(HttpServletRequest request)throws IOException {
		String video = request.getParameter("value");	
		System.out.println("选择注册库视频为："+video);
		//保存下来
		GRegister_video_name.save_tarck_person(video,1);
		//当前注册视频名
		System.out.println("选择的注册视频下的已注册id为：");
		List<String>vid = search_id.search(2,video);
		ModelAndView mView = new ModelAndView();
		mView.addObject("vid",vid);		
		mView.setViewName("Graphnew/Track/TSelectid");
		return mView;
	}
	
	@RequestMapping("/Track_person")
	public ModelAndView Track_p(HttpServletRequest request)throws IOException {
		//得到选择的 id 存储待追踪的人 将其视频展示
		String value = request.getParameter("value");
		System.out.println("确认选择的追踪的人id："+value);
		GRegister_video_name.save_tarck_person(value,2);
		String track_person = GRegister_video_name.get_track_person();
		System.out.println("确认选择的追踪的人："+track_person);
		track_person = track_person+"/"+value+".mp4";
		
		ModelAndView mView = new ModelAndView();
		mView.addObject("track_person",track_person);		
		mView.setViewName("Graphnew/Track/Track_person");
		return mView;
	}
			
	@RequestMapping("/finalResult")
	public ModelAndView finalResult() throws IOException{	
		//调python 追踪
		ArrayList<String> result_path = javaInvokeTrack.Track();
		ModelAndView mView = new ModelAndView();
		mView.addObject("track_person",result_path.get(0));
		mView.addObject("result1",result_path.get(1));
		mView.addObject("result2",result_path.get(2));
		mView.addObject("result3",result_path.get(3));
		mView.addObject("result4",result_path.get(4));
		mView.addObject("result5",result_path.get(5));
		mView.addObject("result6",result_path.get(6));
		mView.setViewName("Graphnew/Track/TResult");
		return mView;
	}
	

	
	
}
