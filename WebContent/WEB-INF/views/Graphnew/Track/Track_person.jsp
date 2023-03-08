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
function confirmEx(){
	return confirm("追踪中，请稍等......");
	}

		 $(document).ready(function ()
				  {
			 	
				     $("#track").submit(function ()
				    		 
				     {	 				    	
				         $.ajax({
				        	 type:'GET',
				        	 url:"<%=request.getContextPath()%>/finalResult",
				        	 data:{value:value},
				        	 async: false,
				        	 success:function(data){
				        		 window.location.href="<%=request.getContextPath()%>/finalResult";
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
		
        .selectid{
        	width: 280px;
            height: 60px;
            margin-top:2px;
            margin-left:2px;
            float:left;
  		/* 	border: 2px solid #2daae1;  */
        }
        	.btn2{
        	width: 180px;
            height: 50px;
  	       /*  border: 1px solid red;  */  
        	}
        #btn_sn2{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
      	    border: 1px solid #2daae1;  
            border-radius: 5px;
            margin-left:160px; 
            margin-top:35px;  
        }
         p{
    
        	font:18px "黑体";
        	
        }
      .id-btn1{
			width: 280px;
        	height: 100px;
           /*   border:2px pink solid;  */
             margin-left:10px;
              margin-top:5px;
             float:left;
		}
		
</style>

<body >

<form id="track" action="finalResult">
<div class="myvideo" style="float:left;" >
	<p>待追踪关注人：</p>
	<video width="450" height="350" loop="loop" autoplay="autoplay" controls="controls"style="margin-left:10px;">
	<source src="/Register_video/${requestScope.track_person}" type="video/mp4"></source>
	</video>
	</div>
	<div class="btn2">
	<input type="submit" id="btn_sn2" value="开始追踪" onclick="confirmEx()" >
	</div>
		</div>	
</form>

</body>
</html>