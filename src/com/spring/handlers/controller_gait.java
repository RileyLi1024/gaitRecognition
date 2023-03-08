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


public class controller_gait {
	int flag = 1;//判断当前是1DCNN预测还是LSTM
	//跳转页面
	@RequestMapping("/showCNN")
	public String showCNN() {
		return "LSTM_1D/1DCNN";
	}
 
	
	//2017毕设1DCNN可以走通 
	
	
   //计算&动态展示
	@RequestMapping("/newextractgait")
	public ModelAndView newextractgait(@RequestParam("firstperson")MultipartFile file_1,@RequestParam("secondperson")MultipartFile file_2) throws IOException {
		String file_1_name=file_1.getOriginalFilename();
		
		String file_2_name=file_2.getOriginalFilename();
		
		try {
			file_1.transferTo(new File("E:\\3DhumanPose-GPU\\input\\video\\"+file_1.getOriginalFilename())); 
			
			file_2.transferTo(new File("E:\\3DhumanPose-GPU\\input\\video\\"+file_2.getOriginalFilename()));
		} catch (IllegalStateException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	//视频1结果放在output1中
//	javaInvokeOpenpose.execPy(file_1_name,"v"); 
	//拷贝结果
//	FileCopy.main(null);
	//视频2结果放在output中
//	javaInvokeOpenpose.execPy(file_2_name,"v"); 
	//转移视频1特征矩阵对应展示图片
//	calculate_video1.transfor();
	//转移视频2特征矩阵对应展示图片
//	calculate_video2.transfor();
	//动态展示界面
	ModelAndView mView=new ModelAndView();
	 //读取两个文件中以.png结尾图片的名字
	String path ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video1";
	//String names = ""; 
	List<String> filename = new ArrayList<String>();
	try { 
	File f = new File(path); 
	if (f.isDirectory()) 
	{ 
	  File[] fList = f.listFiles();
	  for (int j = 0; j < fList.length; j++) { 
	  File file = fList[j]; 
	  if (file.isFile()) 
	  { //这里其实也没有必要 这个文件里肯定全是png啦
		 if(file.getName().endsWith(".png")) {
		  filename.add(file.getName());
		 }
	   }
	 } 
	}
	} catch (Exception e) 
	{
	}
	
	
	String path_two ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video2";
	List<String> filename_two = new ArrayList<String>();;
	try { 
	File f = new File(path_two); 
	if (f.isDirectory()) 
	{ 
	  File[] fList = f.listFiles();
	  for (int j = 0; j < fList.length; j++) { 
	  File file = fList[j]; 
	  if (file.isFile()) 
	  { 
		 if(file.getName().endsWith(".png")) {
		  filename_two.add(file.getName());
		 }
	   }
	 } 
	}
	} catch (Exception e) 
	{
	}
	//打印一下两个链表中的名字
	for(int i =0;i<filename.size();i++) {
		System.out.println("这是video1:"+filename.get(i));}
		
	for(int n =0;n<filename_two.size();n++) {
		System.out.println("这是viedeo2:"+filename_two.get(n));
	}
	
	
	//将链表内容传给前端
	try {
		
		mView.addObject("filename", filename);
		mView.addObject("filename_two", filename_two);
	} catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	//判断当前是什么预测 上面的过程出现一遍
	if(flag == 1)
		mView.setViewName("LSTM_1D/1DCNN_cal");
	else
		mView.setViewName("LSTM_1D/LSTM_cal");
	
	return mView;

	}
	
	//真正计算两个矩阵的代码
	@RequestMapping("/calmatrix")
	public ModelAndView calmatrix() {
		//计算视频1的特征矩阵
		calculate_video1.calculate_matrix();
		//计算视频2的特征矩阵
		calculate_video2.calculate_matrix();
		//动态展示界面
		ModelAndView mView=new ModelAndView();
		 //读取两个文件中以.png结尾图片的名字
		String path ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video1";
		//String names = ""; 
		List<String> filename = new ArrayList<String>();
		try { 
		File f = new File(path); 
		if (f.isDirectory()) 
		{ 
		  File[] fList = f.listFiles();
		  for (int j = 0; j < fList.length; j++) { 
		  File file = fList[j]; 
		  if (file.isFile()) 
		  { //这里其实也没有必要 这个文件里肯定全是png啦
			 if(file.getName().endsWith(".png")) {
			  filename.add(file.getName());
			 }
		   }
		 } 
		}
		} catch (Exception e) 
		{
		}
		
		
		String path_two ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video2";
		List<String> filename_two = new ArrayList<String>();;
		try { 
		File f = new File(path_two); 
		if (f.isDirectory()) 
		{ 
		  File[] fList = f.listFiles();
		  for (int j = 0; j < fList.length; j++) { 
		  File file = fList[j]; 
		  if (file.isFile()) 
		  { 
			 if(file.getName().endsWith(".png")) {
			  filename_two.add(file.getName());
			 }
		   }
		 } 
		}
		} catch (Exception e) 
		{
		}
		//打印一下两个链表中的名字
		for(int i =0;i<filename.size();i++) {
			System.out.println("这是video1:"+filename.get(i));}
			
		for(int n =0;n<filename_two.size();n++) {
			System.out.println("这是viedeo2:"+filename_two.get(n));
		}
		
		
		//将链表内容传给前端
		try {
			
			mView.addObject("filename", filename);
			mView.addObject("filename_two", filename_two);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//判断当前是什么预测 上面的过程出现一遍
		if(flag == 1)
			mView.setViewName("LSTM_1D/1DCNN_process");
		else
			mView.setViewName("LSTM_1D/LSTM_process");
		
		return mView;
	}
	
	
	
	//结果(进行步态提取和相似度分析)
		@RequestMapping("/resultone")
		public String resultone(HttpServletRequest request){
			//这里进行步态特征提取和相似度分析
			
			//假设这是相似度：
			String similarity="test1.123";
			//假设这是结果
			String fruit="二者不是同一个人";
			
//			 //读取两个文件中以.png结尾图片的名字
			String path ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video1";
			//String names = ""; 
			List<String> filename = new ArrayList<String>();
			try { 
			File f = new File(path); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { //这里其实也没有必要 这个文件里肯定全是png啦
				 if(file.getName().endsWith(".png")) {
				  filename.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			
			
			String path_two ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video2";
			List<String> filename_two = new ArrayList<String>();;
			try { 
			File f = new File(path_two); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { 
				 if(file.getName().endsWith(".png")) {
				  filename_two.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			
			
			
			//将链表内容传给前端
			try {
				
				request.setAttribute("filename", filename);
				request.setAttribute("filename_two", filename_two);
				request.setAttribute("similarity", similarity);
				request.setAttribute("fruit", fruit);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
			return "LSTM_1D/1D_result";
		}
	
		@RequestMapping("/resulttwo")
		public String resulttwo(HttpServletRequest request){
			//这里进行步态特征提取和相似度分析
			String similarity=NetAndSimilarity.compute();
			//结果
			double sim = Double.parseDouble(similarity);
			String fruit="";
			if(sim <= 0.35)
				fruit = "二者不是同一个人";
			else
				fruit = "二者是同一个人";
			
//			 //读取两个文件中以.png结尾图片的名字
			String path ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video1";
			//String names = ""; 
			List<String> filename = new ArrayList<String>();
			try { 
			File f = new File(path); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { //这里其实也没有必要 这个文件里肯定全是png啦
				 if(file.getName().endsWith(".png")) {
				  filename.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			
			
			String path_two ="E:\\3DhumanPose-GPU\\Gait-zhangdi\\picture\\video2";
			List<String> filename_two = new ArrayList<String>();;
			try { 
			File f = new File(path_two); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { 
				 if(file.getName().endsWith(".png")) {
				  filename_two.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			
			
			
			//将链表内容传给前端
			try {
				
				request.setAttribute("filename", filename);
				request.setAttribute("filename_two", filename_two);
				request.setAttribute("similarity", similarity);
				request.setAttribute("fruit", fruit);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
			return "LSTM_1D/LSTM_result";
		}
	

		
//毕设1DCNN可以走通 现在在LSTM里面实验界面
		@RequestMapping("/showLSTM")
		public String showLSTM() {
			flag = 0;
			//把output、output1、Matrix文件夹中的内容删除 
 		//	empty_folder.main();
			return "LSTM_1D/LSTM";
		}
		

@RequestMapping("/val_video")
	public ModelAndView val_video(HttpServletRequest request) throws IOException {
		ModelAndView mView=new ModelAndView();
		   String fp = request.getParameter("f1");
		   String sp = request.getParameter("f2");
		    //  System.out.println("val_video一开始接收到的"+fp+sp);
		   //这里接收到的是：C:\fakepath\cat.mp4 截取文件名
		   
		   String flag ="h";
		   int a = fp.indexOf(flag);
		   fp = fp.substring(a+2);
		   sp = sp.substring(a+2);
		   System.out.println("val_video接收到的"+fp+sp);
		  
		   
		  // System.out.println(a);
			mView.addObject("video1", fp);
			mView.addObject("video2", sp);
			
			mView.setViewName("LSTM_1D/val_video");
			
	
			//视频1结果放在output1中
			javaInvokeOpenpose.execPy(fp,"v"); 
			//拷贝结果
			FileCopy.main(null);
			//视频2结果放在output中
			javaInvokeOpenpose.execPy(sp,"v"); 
			
			return mView;
	}
		
@RequestMapping("/LSTM_process")
public ModelAndView val_picture() throws IOException {
	
			//计算视频1的特征矩阵
			calculate_video1.calculate_matrix();
			//计算视频2的特征矩阵
			calculate_video2.calculate_matrix();
			//重命名两视频对应的50帧图片 使其可以按照顺序播放
			rename_p.main();
			//动态展示界面
			ModelAndView mView=new ModelAndView();
			 //读取两个文件中以.png结尾图片的名字
			
			String path ="E:\\workspace-sts\\Gait\\picture\\video1";
			//String names = ""; 
			List<String> filename = new ArrayList<String>();
			try { 
			File f = new File(path); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { //这里其实也没有必要 这个文件里肯定全是png啦
				 if(file.getName().endsWith(".png")) {
				  filename.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			
			
			String path_two ="E:\\workspace-sts\\Gait\\picture\\video2";
			
			List<String> filename_two = new ArrayList<String>();;
			try { 
			File f = new File(path_two); 
			if (f.isDirectory()) 
			{ 
			  File[] fList = f.listFiles();
			  for (int j = 0; j < fList.length; j++) { 
			  File file = fList[j]; 
			  if (file.isFile()) 
			  { 
				 if(file.getName().endsWith(".png")) {
				  filename_two.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			//打印一下两个链表中的名字
			for(int i =0;i<filename.size();i++) {
				System.out.println("这是video1:"+filename.get(i));}
				
			for(int n =0;n<filename_two.size();n++) {
				System.out.println("这是viedeo2:"+filename_two.get(n));
			}
			
			System.out.println("这是val_picture!!!");
			
			
			
			try {
				
				mView.addObject("filename", filename);
				mView.addObject("filename_two", filename_two);
				System.out.println("成功传递!!!");
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
				mView.setViewName("LSTM_1D/LSTM_process");
			
			return mView;
	}

@RequestMapping("/final_result")
public String result(HttpServletRequest request){
	//这里进行步态特征提取和相似度分析 调用神经网络
	String similarity=NetAndSimilarity.compute();
	System.out.println("相似度为similarity："+similarity);
	//结果
	double sim = Double.parseDouble(similarity);
	String fruit="";
	if(sim <= 0.35)
		fruit = "二者不是同一个人";
	else
		fruit = "二者是同一个人";
	
	//假设这是相似度：
//	String similarity="test1.123";
	//假设这是结果
//	String fruit="二者是同一个人";
	
//	 //读取两个文件中以.png结尾图片的名字
	String path ="E:\\workspace-sts\\Gait\\picture\\video1";
	//String names = ""; 
	List<String> filename = new ArrayList<String>();
	try { 
	File f = new File(path); 
	if (f.isDirectory()) 
	{ 
	  File[] fList = f.listFiles();
	  for (int j = 0; j < fList.length; j++) { 
	  File file = fList[j]; 
	  if (file.isFile()) 
	  { //这里其实也没有必要 这个文件里肯定全是png啦
		 if(file.getName().endsWith(".png")) {
		  filename.add(file.getName());
		 }
	   }
	 } 
	}
	} catch (Exception e) 
	{
	}
	
	
	String path_two ="E:\\workspace-sts\\Gait\\picture\\video2";
	List<String> filename_two = new ArrayList<String>();;
	try { 
	File f = new File(path_two); 
	if (f.isDirectory()) 
	{ 
	  File[] fList = f.listFiles();
	  for (int j = 0; j < fList.length; j++) { 
	  File file = fList[j]; 
	  if (file.isFile()) 
	  { 
		 if(file.getName().endsWith(".png")) {
		  filename_two.add(file.getName());
		 }
	   }
	 } 
	}
	} catch (Exception e) 
	{
	}
	
	
	
	//将链表内容传给前端
	try {
		
		request.setAttribute("filename", filename);
		request.setAttribute("filename_two", filename_two);
		request.setAttribute("similarity", similarity);
		request.setAttribute("fruit", fruit);
	} catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}

	return "LSTM_1D/LSTM_result";
}



	






}

