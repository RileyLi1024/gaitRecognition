<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 
<!DOCTYPE html>
<html lang="en">
 <style>
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }
        body{
            background: url("image/register_bg.png") no-repeat;
        }
        .rg_layout{
            width: 900px;
            height: 525px;
            border: 5px solid #EEEEEE;
            background-color: white;
            /*让div水平居中*/
            margin: auto;
            margin-top: 15px;
        }
        .rg_left{
            float: left;
            margin: 15px;
            width: 20%;
        }
        .rg_left > p:first-child{
            color: #FFD026;
            font-size: 20px;
        }
        .rg_left > p:last-child{
            color: #A6A6A6;
        }
        .rg_center{
            /*border: 1px solid red;*/
            float: left;
            width: 450px;
            /*margin: 15px;*/
        }
        .rg_right{
            float: right;
            margin: 15px;
        }
        .rg_right > p:first-child{
            font-size: 15px;
        }
        .rg_right p a {
            color: pink;
        }
        .td_left{
            width: 100px;
            text-align: right;
            height: 45px;
        }
        .td_right{
            padding-left: 50px;
        }
        #username,#password,#email,#name,#tel,#checkcode,#birthday{
            width: 251px;
            height: 32px;
            border: 1px solid #A6A6A6;
            /*设置边框圆角*/
            border-radius: 5px;
            padding-left: 10px ;
        }
        #checkcode{
            width: 110px;
        }
        #img_check{
            height: 32px;
            /*设置垂直居中*/
            vertical-align: middle;
        }
        #btn_sub{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
            border: 1px solid #2daae1;
            margin-left:80px;
            margin-top:8px;
            border-radius: 5px;
        }
    </style>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="UTF-8">


</head>

<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">
 
$(document).ready(function ()
		  {
		     
		     $("#vi").submit(function ()
		    		 
		     {	
		    	 var username=$("#username").val();		    	
		    	 var f1=$("#f1").val();
		         $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/video_in",
		        	 data:{username:username,f1:f1},
		        	 async: false,
		        	 success:function(data){
		        		 $("#video_in").html(data);
		        	 },
		        	 error:function(a){
		        		 alert("出错啦...");
		        	 }	        	 
		         })
		         return false;
		     });    
		 })
		  
	
		
	
</script>


<body >



<div class="register" runat="server">
<div class="rg_layout" style="margin-top:55px;">
        <div class="rg_left">
            <p>注册</p>
        </div>
        <div class="rg_center">
            <div class="rg_form">
                <form action="video_in" method="post" id="vi" enctype="multipart/form-data">
                    <table>
                        <tr>
                            <td class="td_left"><label for="username"><span style="font-size:18px">用户名</span></label></td>
                            <td class="td_right"><input type="text" name="username" id="username" placeholder="请输入用户名" required="" value=""></td>
                        </tr>                                                                       <tr>
                            <td class="td_left"><label for="username"><span style="font-size:18px">请导入视频</span></label></td>
                            <td class="td_right"><input type="file" placeholder="001.avi" title="请导入视频1" required="" value="" name="f1" id="f1" class="form-control"></td>
                        </tr>                                                                     					
					   <tr>
                            <td colspan="2" align="center"><input type="submit" id="btn_sub" value="提取关节点坐标"></td>
                        </tr> 
                        
                        </table>  
                  </form>                  												 
					</div>	
			    <div id="video_in" style="clear:both;" >
  		        </div> 
  		        
  		              		
            </div>                 
        </div>
</div>
        
 

</body>
</html>