package com.spring.handlers;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class cal_matrix {

	private static final String pyInterpreterPath = "python";//ע�⣺�������в����ֿ�д��ʱ��exe���治�����һ���ո񡣵������в���һ��д��ʱ��exe����һ��Ҫ���һ���ո�	
	//python����·��
	private static final String createPath = "E:\\workspace-sts\\Gait\\Matrix_Python\\create_csv.py";//���δָ��.py�ļ�����ȫ·������Ĭ�ϴӹ��̵�ǰĿ¼������
	private static final String calPathOne = "E:\\workspace-sts\\Gait\\Matrix_Python\\calculate_csv1.py";
	private static final String calPathTwo = "E:\\workspace-sts\\Gait\\Matrix_Python\\calculate_csv2.py";
	private static final String deletePath = "E:\\workspace-sts\\Gait\\Matrix_Python\\delete_last.py";
	private static final String csv_num = "E:\\workspace-sts\\Gait\\Matrix_Python\\csv_num.py";
	private static final String csv_start = "E:\\workspace-sts\\Gait\\Matrix_Python\\csv_start.py";
	private static final String cal_real1 = "E:\\workspace-sts\\Gait\\Matrix_Python\\cal_real_one.py";
	private static final String cal_real2 = "E:\\workspace-sts\\Gait\\Matrix_Python\\cal_real_two.py";



    //����Ŀ¼���м���csv�ļ�
    public static int query(String path){
        //�����һ��Ŀ¼
    	int num=0;//�浱ǰ�ļ����������ض���׺���ļ���
    	File queryFile = new File(path);
        if (queryFile.isDirectory()){
            //��������ļ��ŵ������У��������
            File[] files = queryFile.listFiles();
            //��������
            for (File fs : files){
                //�������֮����Ŀ¼����ֱ���ٵ���һ�η���  
               // if (fs.isDirectory()) query(fs); ��̫��Ҫ
                //�������֮���׺Ϊ.csv���ļ���ÿ��һ����++num��ͳ�Ƹ�����
                if (fs.isFile() && fs.getName().endsWith(".png")) ++num;
            }
        }
        //����ж������Ŀ¼�������׺Ϊ.csv���ļ���ÿ��һ��Ҳ++num������ͳ��
        if (queryFile.isFile() && queryFile.getName().endsWith(".png")) ++num;
      //  System.out.println("��ǰ���ɵ�pngͼƬ����Ϊ��"+num);
        return num;
    }
    
    //�������������
    public static void create(String path) {
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,createPath,path};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
    	
    }
    
    //���� csv�ļ�����
    public static int csv_num(String path,String filetype) {
    	String number="";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,csv_num,path,filetype};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
				number += line;
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
		System.out.println("��ǰ�ļ���csv�ļ���Ϊ��"+number);
		int num = Integer.parseInt(number);
		return num;
    }
   
    //���� �ļ���ʼ֡��
    public static int csv_start(String path,String filetype) {
    	String number="";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,csv_start,path,filetype};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
				number += line;
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
		System.out.println("csv�ļ���ʼ��Ϊ��"+number);
		int num = Integer.parseInt(number);
		return num;
    }
    
    
    //�����м���������һ
    public static void compute_one(int num1,String path_in,String path_out) {
    	Process proc;
		try {
			String n = ""+num1;
			String[] arguments = new String[] {pyInterpreterPath,calPathOne,n,path_in,path_out};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
    }

    //�����м���������� 
    public static int compute_Two(int num1,int num2,String path_in,String path_out) {
    	//String flag = "";
    	int f = 1;
    	Process proc;
		try {
			String n1 = ""+num1;
			String n2 =""+num2;
			String[] arguments = new String[] {pyInterpreterPath,calPathTwo,n1,n2,path_in,path_out};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				String flag = line; //��ȡ����ֵ
				//System.out.println("flag��:"+flag);
			     f = Integer.parseInt(flag);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
		/*int f = Integer.parseInt(flag);
		System.out.println("f��:"+f);*/
		return f;
    }
    
    //ɾ���м���������������һ��
    public static void delete_Last(String path) {
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,deletePath,path};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
    }
    
    //�����������������
    public static void cal_real2(String path_in,String path_out,String path) {
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,cal_real2,path_in,path_out,path};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
    }
    
    //����������������һ
    public static int[] cal_real1(String path_in,String path_out,String path,String path2) {
    	List<String> picture = new ArrayList<String>();
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,cal_real1,path_in,path_out,path,path2};
			proc = Runtime.getRuntime().exec(arguments);// ִ��py�ļ�
			//���������������ȡ���
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				picture.add(line);//��ȡ����ֵ
				//System.out.println("picture����Щ������"+picture);
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
		
		
		
		//��˳�����ͼƬ������
		int[] picture_p = new int[50];
		for(int n = 0;n<picture.size();n++) {
			System.out.println("picture num:"+picture.get(n));
			int ff = Integer.parseInt(picture.get(n));
			picture_p[n]=ff;
		}
		for(int n=0;n<picture_p.length;n++)
			System.out.println("picture_p num:"+picture_p[n]);

			return picture_p;

    }
    
    //������
	public static void main(String[] args) {
	      
		//������ļ��������Ŀ¼��CSV�ļ�������
//		query(new File(FilePath1));
//		System.out.println("��ǰ�ļ����е�csv�ļ���Ϊ��"+num);

	}
}
