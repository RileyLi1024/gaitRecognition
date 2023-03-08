<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html lang="en">


<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="UTF-8">


</head>

<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">
 
function extract(){
	return confirm("行人提取中，请稍等......");
	} 
		
		
$(document).ready(function ()
		  {
		     
		     $("#select").submit(function ()
		    		 
		     {		  
		    	
		         $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/select",	
		        	 async: false,
		        	 success:function(data){
		        	
		        		 $("#manageVideo").html(data);		
		        	 },
		        	 error:function(a){
		        		 alert("出错啦...");
		        	 }	        	 
		         })
		         return false;
		     });    
		 })		
		
</script>

<style>
 *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }
         .layout{
            width: 1200px;
            height: 460px;
            border: 5px solid #EEEEEE;
            background-color: white;
            /*让div水平居中*/
           
           margin:auto;
   
           
        }

        .manageVideo{
        	width: 500px;
            height: 450px;
            margin-left:50px;
            float:left;
        /*     border: 2px solid #2daae1; */
            background:url("video/loading.gif");
            backgroud-size:30px 30px;
            backgroud-repeat:no-repeat; 
    		background-position: center center;
        }
        .myvideo{
        	width: 500px;
            height: 450px;
            margin-left:30px;
            float:left;
  		/* 	border: 2px solid #2daae1; */
        }
        #btn_s{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
 		    border: 1px solid #2daae1;
            margin-left:150px;
            margin-top:2px;
            border-radius: 5px;
        }
        .text{
        	width: 100px;
            text-align: right;
            height: 30px;
           	font:18px "黑体";
        }
 

    
</style>

<body >

<div class="layout">
	<form action="select" methon="post" id="select" enctype="multipart/form-data">
	<div class="myvideo" >
	<div class = "text">输入视频：</div>
	<video width="450" height="350" loop="loop" autoplay="autoplay" controls="controls"style="margin-left:10px;">
	<source src="/input_video/${requestScope.video}" type="video/mp4"></source>
	</video>
	<input type="submit" id="btn_s" value="行人提取" onclick="extract()"></td>
	</div>
	</form>
	<div class="manageVideo" id="manageVideo"> </div>

</div>



	

</body>
</html>