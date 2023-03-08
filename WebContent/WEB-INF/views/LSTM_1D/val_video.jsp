<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 
<!DOCTYPE html>
<html lang="en">


<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="UTF-8">


</head>

<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">


/* $("#btnn").click(function ()
		 
	     {		  
	    	              
	         $.ajax({
	        	 type:'post',
	        	 url:"system/val_picture",
	        	 data:data,
	        	 async: false,
	        	 success:function(data){
	        		 alert('开始计算！');
	        		 $("#mypicture").html("aaa");
	        	 },
	        	 error:function(a){
	        		 alert("出错啦...");
	        	 }
	        
	        	 
	         })
	         return false;
	     });  */
	     
	//完全没问题可以用2022/3/8
	 	  $("#btnn").click(function(){
			//发送ajax请求
			alert('开始计算！');
			$("#mypicture").load("LSTM_process");
		})   
		  
	
		
	
</script>


<body >
<div class="myvideo" >
	<div class="myvideo1" id="fade_focus" style="float:left;margin-left:65px;margin-right:150px;" >
    <h3><font size="+2"><span style="color:blue;">video1:</span></font></h3>
	<video width="400" height="350" loop="loop" autoplay="autoplay" controls="controls">
	<source src="video/${requestScope.video1}" type="video/mp4"></source>
	</video> 
	</div>
 	<div class="myvideo2" id="fade" style="position:absolute;left:600px;top:220px" >
 	<h3><font size="+2"><span style="color:blue;">video2:</span></font></h3>
	<video width="400" height="350" loop="loop" autoplay="autoplay" controls="controls">
	<source src="video/${requestScope.video2}" type="video/mp4"></source>
	</video> 
	</div>
</div>
	
 <%-- <div class="mypicture">
	<div class="video1" id="fade_focus" style="float:left;margin-left:65px;margin-right:150px;" >
			   <div class="loading">Loading...<br /><img src="/p/loading3.gif" width="350" height="350" /></div>
			   <h3><font size="+2"><span style="color:black;">video1:</span></font></h3>
			   <c:forEach items="${requestScope.filename}" var="name" varStatus="vs">
<!-- 			<p class="font-bold text-success">两个视频中的人为同一人</p> -->
			   <ul>
			   <li><img src="/video1/${name}" width="400" height="350" /></li>
			   </ul>	
			   </c:forEach>		   		   
	    </div>

        <div class="video2" id="fade" style="position:absolute;left:600px;top:610px" >
			  <div class="loading">Loading...<br /><img src="/p/loading3.gif" width="350" height="350" /></div>
			   <h3><font size="+2"><span style="color:black;">video2:</span></font></h3>
			   <c:forEach items="${requestScope.filename_two}" var="name_two" varStatus="vs">
 			   <ul> 
 			   <li><img src="/video2/${name_two}" width="400" height="350"/></li>
			   </ul>	 
			   </c:forEach>	
	    </div>		 	   	
	</div> 
	 --%>
	


<form action="LSTM_process" method="post" id="loginForm" >
	<div>
	<button class="btn btn-success btn-block loginbtn" id = "btnn" type="submit">计算特征矩阵</button>							
	</div>
</form>
	
	

</body>
</html>