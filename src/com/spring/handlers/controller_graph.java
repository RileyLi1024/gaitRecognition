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


public class controller_graph {

	      //��ת��ͼ������� 
			@RequestMapping("/showGaitGraph")
			public String show2StreamNet() {
				//��output��output1��Matrix�ļ����е�����ɾ�� ��֪��Ϊɶû����
	 //			empty_folder.main();
	 			System.out.println("����ͼ����������");
				return "GraphConvolution/GaitGraph";
			}
	
	
@RequestMapping("/val_video_3")
	public ModelAndView val_video_2(HttpServletRequest request) throws IOException {
		ModelAndView mView=new ModelAndView();
		   String fp = request.getParameter("f1");
		   String sp = request.getParameter("f2");
		 //  System.out.println("val_videoһ��ʼ���յ���"+fp+sp);
		   //������յ����ǣ�C:\fakepath\cat.mp4 ��ȡ�ļ���
		   
		   String flag ="h";
		   int a = fp.indexOf(flag);
		   fp = fp.substring(a+2);
		   sp = sp.substring(a+2);
		   System.out.println("ͼ���������յ���"+fp+sp);
		  
		   
		  // System.out.println(a);
			mView.addObject("video1", fp);
			mView.addObject("video2", sp);
			
			mView.setViewName("GraphConvolution/val_video_3");
			
	
			//��Ƶ1�������output1��
		//    javaInvokeOpenpose.execPy(fp,"v"); 
			//�������
		//	FileCopy.main(null);
			//��Ƶ2�������output��
		//	javaInvokeOpenpose.execPy(sp,"v"); 
			
			return mView;
	}
		
@RequestMapping("/GaitGraph_process")
public ModelAndView val_picture() throws IOException {
	
	        System.out.println("ͼ������������������");
			//�������˵�����csv�ļ����������Ϊ������������ľ���
	        gaitgraph_cal.cal_GraphMatrix();
			//��̬չʾ����
			ModelAndView mView=new ModelAndView();
			 //��ȡ�����ļ�����.png��βͼƬ������ ��ʱͼƬ����Matrix_graph.py�Ĵ���Ҳ�Ѿ������� ��˳�򲥷ž���
			
			String path ="E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video";
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
			  { //������ʵҲû�б�Ҫ ����ļ���϶�ȫ��png��
				 if(file.getName().endsWith(".png")) {
				  filename.add(file.getName());
				 }
			   }
			 } 
			}
			} catch (Exception e) 
			{
			}
			
			
			String path_two ="E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output\\video";
			
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
			//��ӡһ�����������е�����
			for(int i =0;i<filename.size();i++) {
				System.out.println("����video1:"+filename.get(i));}
				
			for(int n =0;n<filename_two.size();n++) {
				System.out.println("����viedeo2:"+filename_two.get(n));
			}
			
			System.out.println("����val_picture!!!");
			
			
			
			try {
				
				mView.addObject("filename", filename);
				mView.addObject("filename_two", filename_two);
				System.out.println("�ɹ�����!!!");
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
				mView.setViewName("GraphConvolution/GaitGraph_process");
			
			return mView;
	}

@RequestMapping("/GaitGraph_result")
public String result(HttpServletRequest request){
	//������в�̬������ȡ�����ƶȷ��� ����������
	String result=javaInvokeGaitGraph.compute();
	System.out.println("���Ϊ��"+result);
	//���
	double sim = Double.parseDouble(result);
	String fruit="";
	// �����׼�Լ����� û�ҵ�����
	if(sim <= 0.5)
		fruit = "���߲���ͬһ����";
	else
		fruit = "������ͬһ����";
	
	//�����������ƶȣ�
//	String similarity="test1.123";
	//�������ǽ��
//	String fruit="������ͬһ����";
	
//	 //��ȡ�����ļ�����.png��βͼƬ������
	String path ="E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output1\\video";
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
	  { //������ʵҲû�б�Ҫ ����ļ���϶�ȫ��png��
		 if(file.getName().endsWith(".png")) {
		  filename.add(file.getName());
		 }
	   }
	 } 
	}
	} catch (Exception e) 
	{
	}
	
	
	String path_two ="E:\\workspace-sts\\Gait\\Pose3Dkeypoints\\output\\video";
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
	
	
	
	//���������ݴ���ǰ��
	try {
		
		request.setAttribute("filename", filename);
		request.setAttribute("filename_two", filename_two);
		request.setAttribute("similarity", sim);
		request.setAttribute("fruit", fruit);
	} catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}

	return "GraphConvolution/GaitGraph_result";
}



	






}

