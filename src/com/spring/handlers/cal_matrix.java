package com.spring.handlers;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class cal_matrix {

	private static final String pyInterpreterPath = "python";//注意：当命令行参数分开写的时候，exe后面不用添加一个空格。当命令行参数一起写的时候，exe后面一定要添加一个空格	
	//python代码路径
	private static final String createPath = "E:\\workspace-sts\\Gait\\Matrix_Python\\create_csv.py";//如果未指定.py文件的完全路径，则默认从工程当前目录下搜索
	private static final String calPathOne = "E:\\workspace-sts\\Gait\\Matrix_Python\\calculate_csv1.py";
	private static final String calPathTwo = "E:\\workspace-sts\\Gait\\Matrix_Python\\calculate_csv2.py";
	private static final String deletePath = "E:\\workspace-sts\\Gait\\Matrix_Python\\delete_last.py";
	private static final String csv_num = "E:\\workspace-sts\\Gait\\Matrix_Python\\csv_num.py";
	private static final String csv_start = "E:\\workspace-sts\\Gait\\Matrix_Python\\csv_start.py";
	private static final String cal_real1 = "E:\\workspace-sts\\Gait\\Matrix_Python\\cal_real_one.py";
	private static final String cal_real2 = "E:\\workspace-sts\\Gait\\Matrix_Python\\cal_real_two.py";



    //计算目录下有几个csv文件
    public static int query(String path){
        //如果是一个目录
    	int num=0;//存当前文件夹中满足特定后缀的文件数
    	File queryFile = new File(path);
        if (queryFile.isDirectory()){
            //把里面的文件放到数组中，方便遍历
            File[] files = queryFile.listFiles();
            //遍历数组
            for (File fs : files){
                //如果遍历之后还有目录，就直接再调用一次方法  
               // if (fs.isDirectory()) query(fs); 不太需要
                //如果遍历之后后缀为.csv的文件，每有一个就++num（统计个数）
                if (fs.isFile() && fs.getName().endsWith(".png")) ++num;
            }
        }
        //最后判断最初的目录下如果后缀为.csv的文件，每有一个也++num，进行统计
        if (queryFile.isFile() && queryFile.getName().endsWith(".png")) ++num;
      //  System.out.println("当前生成的png图片个数为："+num);
        return num;
    }
    
    //生成两个输出表
    public static void create(String path) {
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,createPath,path};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
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
    
    //计算 csv文件数量
    public static int csv_num(String path,String filetype) {
    	String number="";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,csv_num,path,filetype};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
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
		System.out.println("当前文件夹csv文件数为："+number);
		int num = Integer.parseInt(number);
		return num;
    }
   
    //计算 文件开始帧数
    public static int csv_start(String path,String filetype) {
    	String number="";
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,csv_start,path,filetype};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
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
		System.out.println("csv文件开始数为："+number);
		int num = Integer.parseInt(number);
		return num;
    }
    
    
    //计算中间特征矩阵一
    public static void compute_one(int num1,String path_in,String path_out) {
    	Process proc;
		try {
			String n = ""+num1;
			String[] arguments = new String[] {pyInterpreterPath,calPathOne,n,path_in,path_out};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
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

    //计算中间特征矩阵二 
    public static int compute_Two(int num1,int num2,String path_in,String path_out) {
    	//String flag = "";
    	int f = 1;
    	Process proc;
		try {
			String n1 = ""+num1;
			String n2 =""+num2;
			String[] arguments = new String[] {pyInterpreterPath,calPathTwo,n1,n2,path_in,path_out};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				String flag = line; //获取返回值
				//System.out.println("flag是:"+flag);
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
		System.out.println("f是:"+f);*/
		return f;
    }
    
    //删除中间特征矩阵二的最后一行
    public static void delete_Last(String path) {
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,deletePath,path};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
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
    
    //计算最终特征矩阵二
    public static void cal_real2(String path_in,String path_out,String path) {
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,cal_real2,path_in,path_out,path};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
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
    
    //计算最终特征矩阵一
    public static int[] cal_real1(String path_in,String path_out,String path,String path2) {
    	List<String> picture = new ArrayList<String>();
    	Process proc;
		try {
			String[] arguments = new String[] {pyInterpreterPath,cal_real1,path_in,path_out,path,path2};
			proc = Runtime.getRuntime().exec(arguments);// 执行py文件
			//用输入输出流来截取结果
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				picture.add(line);//获取返回值
				//System.out.println("picture是这些：：："+picture);
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		} 
		
		
		
		//按顺序构造的图片名序列
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
    
    //主函数
	public static void main(String[] args) {
	      
		//打开输出文件并计算该目录下CSV文件的数量
//		query(new File(FilePath1));
//		System.out.println("当前文件夹中的csv文件数为："+num);

	}
}
