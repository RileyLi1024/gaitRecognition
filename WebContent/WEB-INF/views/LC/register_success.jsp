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
var time = 4;	        
function returnUrlByTime() {  	            
	window.setTimeout('returnUrlByTime()', 1000);  	            
	time = time - 1;  	            
	if(time<=0){	            	
		time = 0;	         
		window.setTimeout("location.href='${pageContext.request.contextPath}/showLC';", 0);
		}	            
	document.getElementById("layer").innerHTML = time;  	        
	}  		
	</script>
	<body onload="returnUrlByTime()"> 
	<div >
	<a href="javascript:void(0)" onclick="window.location.href='${pageContext.request.contextPath}/showLC' " >
	
	<font size="2px" >${requestScope.result}<b><span id="layer">3</span></b>秒后会自动跳转，如果没有跳转，请点这里......</font></a>
	</div>
	</body>



</html>