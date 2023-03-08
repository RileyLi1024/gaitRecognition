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
	int flag = 1;//�жϵ�ǰ��1DCNNԤ�⻹��LSTM
	//��תҳ��
	@RequestMapping("/showCNN")
	public String showCNN() {
		return "LSTM_1D/1DCNN";
	}
 
	
	//2017����1DCNN������ͨ 
	
	
   //����&��̬չʾ
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
	//��Ƶ1�������output1��
//	javaInvokeOpenpose.execPy(file_1_name,"v"); 
	//�������
//	FileCopy.main(null);
	//��Ƶ2�������output��
//	javaInvokeOpenpose.execPy(file_2_name,"v"); 
	//ת����Ƶ1���������ӦչʾͼƬ
//	calculate_video1.transfor();
	//ת����Ƶ2���������ӦչʾͼƬ
//	calculate_video2.transfor();
	//��̬չʾ����
	ModelAndView mView=new ModelAndView();
	 //��ȡ�����ļ�����.png��βͼƬ������
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
	//��ӡһ�����������е�����
	for(int i =0;i<filename.size();i++) {
		System.out.println("����video1:"+filename.get(i));}
		
	for(int n =0;n<filename_two.size();n++) {
		System.out.println("����viedeo2:"+filename_two.get(n));
	}
	
	
	//���������ݴ���ǰ��
	try {
		
		mView.addObject("filename", filename);
		mView.addObject("filename_two", filename_two);
	} catch (Exception e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	//�жϵ�ǰ��ʲôԤ�� ����Ĺ��̳���һ��
	if(flag == 1)
		mView.setViewName("LSTM_1D/1DCNN_cal");
	else
		mView.setViewName("LSTM_1D/LSTM_cal");
	
	return mView;

	}
	
	//����������������Ĵ���
	@RequestMapping("/calmatrix")
	public ModelAndView calmatrix() {
		//������Ƶ1����������
		calculate_video1.calculate_matrix();
		//������Ƶ2����������
		calculate_video2.calculate_matrix();
		//��̬չʾ����
		ModelAndView mView=new ModelAndView();
		 //��ȡ�����ļ�����.png��βͼƬ������
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
		//��ӡһ�����������е�����
		for(int i =0;i<filename.size();i++) {
			System.out.println("����video1:"+filename.get(i));}
			
		for(int n =0;n<filename_two.size();n++) {
			System.out.println("����viedeo2:"+filename_two.get(n));
		}
		
		
		//���������ݴ���ǰ��
		try {
			
			mView.addObject("filename", filename);
			mView.addObject("filename_two", filename_two);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//�жϵ�ǰ��ʲôԤ�� ����Ĺ��̳���һ��
		if(flag == 1)
			mView.setViewName("LSTM_1D/1DCNN_process");
		else
			mView.setViewName("LSTM_1D/LSTM_process");
		
		return mView;
	}
	
	
	
	//���(���в�̬��ȡ�����ƶȷ���)
		@RequestMapping("/resultone")
		public String resultone(HttpServletRequest request){
			//������в�̬������ȡ�����ƶȷ���
			
			//�����������ƶȣ�
			String similarity="test1.123";
			//�������ǽ��
			String fruit="���߲���ͬһ����";
			
//			 //��ȡ�����ļ�����.png��βͼƬ������
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
			
			
			
			//���������ݴ���ǰ��
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
			//������в�̬������ȡ�����ƶȷ���
			String similarity=NetAndSimilarity.compute();
			//���
			double sim = Double.parseDouble(similarity);
			String fruit="";
			if(sim <= 0.35)
				fruit = "���߲���ͬһ����";
			else
				fruit = "������ͬһ����";
			
//			 //��ȡ�����ļ�����.png��βͼƬ������
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
			
			
			
			//���������ݴ���ǰ��
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
	

		
//����1DCNN������ͨ ������LSTM����ʵ�����
		@RequestMapping("/showLSTM")
		public String showLSTM() {
			flag = 0;
			//��output��output1��Matrix�ļ����е�����ɾ�� 
 		//	empty_folder.main();
			return "LSTM_1D/LSTM";
		}
		

@RequestMapping("/val_video")
	public ModelAndView val_video(HttpServletRequest request) throws IOException {
		ModelAndView mView=new ModelAndView();
		   String fp = request.getParameter("f1");
		   String sp = request.getParameter("f2");
		    //  System.out.println("val_videoһ��ʼ���յ���"+fp+sp);
		   //������յ����ǣ�C:\fakepath\cat.mp4 ��ȡ�ļ���
		   
		   String flag ="h";
		   int a = fp.indexOf(flag);
		   fp = fp.substring(a+2);
		   sp = sp.substring(a+2);
		   System.out.println("val_video���յ���"+fp+sp);
		  
		   
		  // System.out.println(a);
			mView.addObject("video1", fp);
			mView.addObject("video2", sp);
			
			mView.setViewName("LSTM_1D/val_video");
			
	
			//��Ƶ1�������output1��
			javaInvokeOpenpose.execPy(fp,"v"); 
			//�������
			FileCopy.main(null);
			//��Ƶ2�������output��
			javaInvokeOpenpose.execPy(sp,"v"); 
			
			return mView;
	}
		
@RequestMapping("/LSTM_process")
public ModelAndView val_picture() throws IOException {
	
			//������Ƶ1����������
			calculate_video1.calculate_matrix();
			//������Ƶ2����������
			calculate_video2.calculate_matrix();
			//����������Ƶ��Ӧ��50֡ͼƬ ʹ����԰���˳�򲥷�
			rename_p.main();
			//��̬չʾ����
			ModelAndView mView=new ModelAndView();
			 //��ȡ�����ļ�����.png��βͼƬ������
			
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
		
				mView.setViewName("LSTM_1D/LSTM_process");
			
			return mView;
	}

@RequestMapping("/final_result")
public String result(HttpServletRequest request){
	//������в�̬������ȡ�����ƶȷ��� ����������
	String similarity=NetAndSimilarity.compute();
	System.out.println("���ƶ�Ϊsimilarity��"+similarity);
	//���
	double sim = Double.parseDouble(similarity);
	String fruit="";
	if(sim <= 0.35)
		fruit = "���߲���ͬһ����";
	else
		fruit = "������ͬһ����";
	
	//�����������ƶȣ�
//	String similarity="test1.123";
	//�������ǽ��
//	String fruit="������ͬһ����";
	
//	 //��ȡ�����ļ�����.png��βͼƬ������
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
	
	
	
	//���������ݴ���ǰ��
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

