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
	return confirm("判别中，请稍等......");
	}
		
		
$(document).ready(function ()
		  {
		     
		     $("#dr").submit(function ()
		    		 
		     {		                 
		         $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/distinguish_result",	
		        	 async: false,
		        	 success:function(data){
		        	
		        		 $("#dis_result").html(data);
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
        .rg_center{
            /*border: 1px solid red;*/
            float: left;
            width: 450px;
            /*margin: 15px;*/
        }
        #btn_s{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
            border: 1px solid #2daae1;
            margin-left:170px;
            margin-top:2px;
            border-radius: 5px;
        }	
		
</style>

<body >
<div class="myvideo" style="margin-top:10px;margin-left:35px">
	<div class="myvideo1" id="fade_focus" style="float:left;margin-left:25px;margin-right:150px;" >
	<video width="400" height="280" loop="loop" autoplay="autoplay" controls="controls">
	<source src="/video/${requestScope.video}" type="video/mp4"></source>
	</video> 
	</div>
</div>
	

<div class="rg_center">
<form action="distinguish_result" method="post" id="dr" >
	<table>
	<tr>
     <td colspan="2" align="center"><input type="submit" id="btn_s" value="判别" onclick="confirmEx()"></td>
     </tr> 
	</table>
</form>
		</div>
		
<div id="dis_result" style="float:left;margin-left:80px;">
			
		</div>

	

</body>
</html>