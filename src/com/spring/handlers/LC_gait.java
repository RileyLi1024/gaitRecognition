package com.spring.handlers;

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
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;

//import com.models.JointData;
import com.sun.net.httpserver.Authenticator.Success;
import java.io.*;



@Controller


public class LC_gait {
	//跳转页面
	@RequestMapping("/showLC")
	public String showLC() {
		return "LC/LC_PoseGait";
	}
	
	//注册
	@RequestMapping("/LC_register")
	public String register() {
		System.out.println("register页面！");
		return "LC/LC_register";
	}
	
	// 存视频是否已注册 0：未注册，注册成功 1：已注册
	public static int flag1 = 0;
	
	@RequestMapping("/video_in")
	public ModelAndView video(HttpServletRequest request) throws IOException {
		System.out.println("video_in页面！");
		ModelAndView mView = new ModelAndView();
		String username = request.getParameter("username");
		String f1 = request.getParameter("f1");
		
		String flag ="h";
		int a = f1.indexOf(flag);
		f1 = f1.substring(a+2);
		
		System.out.println("注册视频：");
		System.out.println("用户名："+username);
		System.out.println("视频名："+f1);
		
		mView.addObject("video", f1);
		mView.setViewName("LC/video_in");
		
		//调取Openpose提取关节点并计算特征矩阵 video2是因为这个计算的就是output文件夹的关节点 ！！！注意算出的特征矩阵存放路径
		javaInvokeOpenpose.execPy(f1,"v"); 
		calculate_video2.calculate_matrix();		
		//视频结果按照用户名和视频名创建文件夹存放 (目前的逻辑还是 先计算有结果了 移动的时候发现存在了就已注册)
		 flag1 = create_file.create(username, f1);	
		 //根据两特征矩阵调用神经网络计算特征向量 **这里没写好 py需要写成接收两个变量，单独算特征向量算出来之后输出到Register//username//matrix1_f1.csv 里
		 LstmCnn_Net.compute_matrix(username, f1);
		return mView;
	}
	
	//计算特征矩阵
	@RequestMapping("/register_result")
	public ModelAndView rresult() {
		System.out.println("显示注册结果！");
		String result ;
		if(flag1 == 0)
			result = "恭喜您注册成功，";
		else
			result = "该视频已注册，";
		ModelAndView mView = new ModelAndView();
		mView.addObject("result", result);
		mView.setViewName("LC/register_success");
		return mView;
	}

	
	//判别
	@RequestMapping("/distinguish")
	public String distinguish() {
		System.out.println("判别页面！");
		return "LC/LC_distinguish";
	}
	
	@RequestMapping("/video_out")
	public ModelAndView videoo(HttpServletRequest request) throws IOException {
		System.out.println("video_out页面！");
		ModelAndView mView = new ModelAndView();
		String f2 = request.getParameter("f2");
		
		String flag ="h";
		int a = f2.indexOf(flag);
		f2 = f2.substring(a+2);
		
		System.out.println("待判别视频：");
		System.out.println("视频名："+f2);
		
		mView.addObject("video", f2);
		mView.setViewName("LC/video_out");
		
		//提取关节点,并计算特征矩阵 注意算出之后的路径！！！！
		javaInvokeOpenpose.execPy(f2,"v"); 
		calculate_video2.calculate_matrix();
		 //根据两特征矩阵调用神经网络计算特征向量 **这里没写好 py需要写成接收两个变量，判断第一个是不是空的 空的就给 判别视频的特征矩阵的路径 单独算特征向量算出来 
		LstmCnn_Net.compute_matrix("", f2);
		return mView;
	}
	
	
	@RequestMapping("/distinguish_result")
	public ModelAndView dis_result() throws IOException {
		System.out.println("显示判别结果！");
		//找到Register里每个username对应的所有特征向量
		String fruit="";
		String result = LC_getsim.main(null);
		//String result = "maomao~";
		//String result ="";
		if (result == "") {
			fruit = "该用户未注册！请注册^-^";
		}
		else
			fruit = "该用户为"+result;		
		
		ModelAndView mView = new ModelAndView();
		
		mView.addObject("result", fruit);
		mView.setViewName("LC/distinguish_result");
		
		return mView;
	}
}

