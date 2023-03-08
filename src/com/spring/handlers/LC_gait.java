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
	//��תҳ��
	@RequestMapping("/showLC")
	public String showLC() {
		return "LC/LC_PoseGait";
	}
	
	//ע��
	@RequestMapping("/LC_register")
	public String register() {
		System.out.println("registerҳ�棡");
		return "LC/LC_register";
	}
	
	// ����Ƶ�Ƿ���ע�� 0��δע�ᣬע��ɹ� 1����ע��
	public static int flag1 = 0;
	
	@RequestMapping("/video_in")
	public ModelAndView video(HttpServletRequest request) throws IOException {
		System.out.println("video_inҳ�棡");
		ModelAndView mView = new ModelAndView();
		String username = request.getParameter("username");
		String f1 = request.getParameter("f1");
		
		String flag ="h";
		int a = f1.indexOf(flag);
		f1 = f1.substring(a+2);
		
		System.out.println("ע����Ƶ��");
		System.out.println("�û�����"+username);
		System.out.println("��Ƶ����"+f1);
		
		mView.addObject("video", f1);
		mView.setViewName("LC/video_in");
		
		//��ȡOpenpose��ȡ�ؽڵ㲢������������ video2����Ϊ�������ľ���output�ļ��еĹؽڵ� ������ע�����������������·��
		javaInvokeOpenpose.execPy(f1,"v"); 
		calculate_video2.calculate_matrix();		
		//��Ƶ��������û�������Ƶ�������ļ��д�� (Ŀǰ���߼����� �ȼ����н���� �ƶ���ʱ���ִ����˾���ע��)
		 flag1 = create_file.create(username, f1);	
		 //���������������������������������� **����ûд�� py��Ҫд�ɽ��������������������������������֮�������Register//username//matrix1_f1.csv ��
		 LstmCnn_Net.compute_matrix(username, f1);
		return mView;
	}
	
	//������������
	@RequestMapping("/register_result")
	public ModelAndView rresult() {
		System.out.println("��ʾע������");
		String result ;
		if(flag1 == 0)
			result = "��ϲ��ע��ɹ���";
		else
			result = "����Ƶ��ע�ᣬ";
		ModelAndView mView = new ModelAndView();
		mView.addObject("result", result);
		mView.setViewName("LC/register_success");
		return mView;
	}

	
	//�б�
	@RequestMapping("/distinguish")
	public String distinguish() {
		System.out.println("�б�ҳ�棡");
		return "LC/LC_distinguish";
	}
	
	@RequestMapping("/video_out")
	public ModelAndView videoo(HttpServletRequest request) throws IOException {
		System.out.println("video_outҳ�棡");
		ModelAndView mView = new ModelAndView();
		String f2 = request.getParameter("f2");
		
		String flag ="h";
		int a = f2.indexOf(flag);
		f2 = f2.substring(a+2);
		
		System.out.println("���б���Ƶ��");
		System.out.println("��Ƶ����"+f2);
		
		mView.addObject("video", f2);
		mView.setViewName("LC/video_out");
		
		//��ȡ�ؽڵ�,�������������� ע�����֮���·����������
		javaInvokeOpenpose.execPy(f2,"v"); 
		calculate_video2.calculate_matrix();
		 //���������������������������������� **����ûд�� py��Ҫд�ɽ��������������жϵ�һ���ǲ��ǿյ� �յľ͸� �б���Ƶ�����������·�� ������������������� 
		LstmCnn_Net.compute_matrix("", f2);
		return mView;
	}
	
	
	@RequestMapping("/distinguish_result")
	public ModelAndView dis_result() throws IOException {
		System.out.println("��ʾ�б�����");
		//�ҵ�Register��ÿ��username��Ӧ��������������
		String fruit="";
		String result = LC_getsim.main(null);
		//String result = "maomao~";
		//String result ="";
		if (result == "") {
			fruit = "���û�δע�ᣡ��ע��^-^";
		}
		else
			fruit = "���û�Ϊ"+result;		
		
		ModelAndView mView = new ModelAndView();
		
		mView.addObject("result", fruit);
		mView.setViewName("LC/distinguish_result");
		
		return mView;
	}
}

