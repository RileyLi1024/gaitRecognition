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

/* function confirmEx(){
	return confirm("注册中，请稍等......");
	}
		 */
		
$(document).ready(function ()
		  {
		     
		     $("#ri").submit(function ()
		    		 
		     {		 
		    	  var id = $('#registerID option:selected').val();
		    	 $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/RegisterID",	
		        	 async: false,
		        	 data:{id:id},
		        	 success:function(data){
		        	
		        		 alert("成功将id传到后端！");
		        	
		        		 $("#result").html(data);
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
		
		
		.id-btn{
			width: 550px;
        	height: 50px;
        	/* border:2px #ffff00 solid; */
		}
        .selectID{
        	width: 250px;
            height: 60px;
            margin-top:2px;
            margin-left:2px;
            float:left;
  		/* 	border: 2px solid #2daae1; */
        }
        select{
        	width: 249px;
        	height: 30px;
        	font-size:18px;
        	text-align:center;
        /* 	border:2px #2daae1 solid; */
        	}
        	.btn{
        	width: 200px;
            height: 60px;
  
        	}
        #btn_sn{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
      	    border: 1px solid #2daae1; 
            margin-top:10px;  
            border-radius: 5px;   
            float:left;
        }
		 p{
        	font:18px "黑体";
        }
     .result{
    
     width: 150px;
     height: 40px;
     margin-left:120px;
     margin-top:20px;
     
     }
        
</style>

<body >

<div class="vv">
	<p>行人提取后视频：</p>
	<video width="450" height="350" loop="loop" autoplay="autoplay" controls="controls" style="margin-left:10px;margin-top:5px;">
	<source src="/output_video/${requestScope.video}/${requestScope.register_vname}" type="video/mp4"></source>
	</video> 
</div>

<form id="ri">
<div class="id-btn">
	<div class="selectID" style="float:left;">
	<p style="font:18px "黑体";">选择注册ID：</p>
		<select name="registerID" id="registerID" runat="server"  >
			 <c:forEach items="${requestScope.id_name}" var="item" varStatus="vs">
            	<option value="${item}">${item}</option>
            </c:forEach> 
            <%-- <option value="${requestScope.id_name}">${requestScope.id_name}</option> --%>

		</select>
	</div>
	<div class="btn">
	<input type="submit" id="btn_sn" value="注册"></td>
	<div class="result" id="result"></div>
	</div>
	</div>
	</form>

	

</body>
</html>