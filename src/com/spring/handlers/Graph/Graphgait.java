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
	//ע��
	@RequestMapping("/GraphRegister")
	public String showGR() {
		System.out.println("registerҳ�棡");
		return "Graphnew/Register/Register";
	}
	
	@RequestMapping("/videoReading")
	public ModelAndView video(HttpServletRequest request) throws IOException {
		System.out.println("videoReadingҳ�棡");
		ModelAndView mView = new ModelAndView();
		String realpath = request.getParameter("f1");
		
		String flag ="h";
		int a = realpath.indexOf(flag);
		String video_name = realpath.substring(a+2);

		System.out.println("ע����Ƶ����"+video_name);
		//����ע����Ƶ�� ������һ��ע����Ƶ���ļ���
		GRegister_video_name.save_video_name(video_name);
		create_file.create(video_name);
		
		mView.addObject("video", video_name);
		mView.setViewName("Graphnew/Register/videoReading");

		return mView;
	}

	/*
	 * @RequestMapping("/searchId") public String[] searchId() { String[] id_name =
	 * null; id_name = search_id.search(); System.out.println("����IDΪ��"); for(int i =
	 * 0;i<id_name.length;i++) { System.out.println(id_name[i]); } return id_name; }
	 */
	
	
	@RequestMapping("/select")
	public ModelAndView select(){
		//��ǰע����Ƶ��
		String video = traverse_id.get_rname();
		System.out.println("ע����ȡ�õ���Ƶ��Ϊ��"+video);
		//��py����ǰ��Ƶ �����浽��Ӧ��Ƶ���ļ����� �õ���������Ƶ��
		//����Ƶ�Ƿ����
		boolean n = search_processed.search(video);
		if(n)
			{javaInvokeGraph.extract();}
		//�������Ƶ��
		String register_vname = "Extracted"+video+".mp4";
		System.out.println("��ȡ�õ���Ƶ��Ϊ��"+register_vname);	
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
		
		//�õ�ѡ���ע��ID ��py����ӦID����Ƶ���浽���潨���Ǹ�ע����Ƶ���ļ�����
		String id = request.getParameter("id");
		System.out.println("����ѡ��ע���ID��"+id);
		// �ж��Ƿ��ظ�ע�� ����register�ļ��� ���Ƿ�ǰע��video_name�ļ����� ������ѡ���id�ļ�
		String result = "";
		int flag ;
		flag = traverse_id.traverse(id);
		
		System.out.println("flag="+flag);
		if(flag == 1) {
			javaInvokeCreateID.create_id_video(id);
			result = "ע��ɹ���";
		}
		else if(flag == 0) result = "��id��ע�ᣡ";
					
		
		ModelAndView mView = new ModelAndView();
		mView.addObject("result", result);
		mView.setViewName("Graphnew/Register/Rresult");
		return mView;
	
	}
	
	@RequestMapping("/test")
	public String showG() {
		System.out.println("testvideoҳ�棡");
		return "Graphnew/testvideo";
	}
	
	
	
	
	//������׷��
	@RequestMapping("/GraphTrack")
	public String showGD() {
		System.out.println("Trackҳ�棡");
		return "Graphnew/Track/Track";
	}
	
	
	@RequestMapping("/TSelectvideo")
	public ModelAndView TVideo(HttpServletRequest request) throws IOException {
		System.out.println("������ȡ�õ���Ƶ �Լ�ѡ��ע����е�ID��");
		//��ǰע����Ƶ��
		String f1 = request.getParameter("f1");
		
		String flag ="h";
		int a = f1.indexOf(flag);
		String video_name = f1.substring(a+2);

		System.out.println("�����׷����Ƶ����"+video_name);
		//�����׷����Ƶ����video_name.txt  video_name.txt��Զ����������ȡ����Ƶ��
		GRegister_video_name.save_video_name(video_name);
		//��py����ǰ��Ƶ �����浽��Ӧ��Ƶ���ļ����� �õ���������Ƶ��
		//����Ƶ�Ƿ����
		String video = video_name.replace(".mp4", "");
		if(search_processed.search(video))
			{javaInvokeGraph.extract();}
		//�������Ƶ��
		String track_vname = "Extracted"+video+".mp4";
		System.out.println("��ȡ�õ���Ƶ��Ϊ��"+track_vname);			
		//��ǰע����Ƶ
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
		System.out.println("ѡ��ע�����ƵΪ��"+video);
		//��������
		GRegister_video_name.save_tarck_person(video,1);
		//��ǰע����Ƶ��
		System.out.println("ѡ���ע����Ƶ�µ���ע��idΪ��");
		List<String>vid = search_id.search(2,video);
		ModelAndView mView = new ModelAndView();
		mView.addObject("vid",vid);		
		mView.setViewName("Graphnew/Track/TSelectid");
		return mView;
	}
	
	@RequestMapping("/Track_person")
	public ModelAndView Track_p(HttpServletRequest request)throws IOException {
		//�õ�ѡ��� id �洢��׷�ٵ��� ������Ƶչʾ
		String value = request.getParameter("value");
		System.out.println("ȷ��ѡ���׷�ٵ���id��"+value);
		GRegister_video_name.save_tarck_person(value,2);
		String track_person = GRegister_video_name.get_track_person();
		System.out.println("ȷ��ѡ���׷�ٵ��ˣ�"+track_person);
		track_person = track_person+"/"+value+".mp4";
		
		ModelAndView mView = new ModelAndView();
		mView.addObject("track_person",track_person);		
		mView.setViewName("Graphnew/Track/Track_person");
		return mView;
	}
			
	@RequestMapping("/finalResult")
	public ModelAndView finalResult() throws IOException{	
		//��python ׷��
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
