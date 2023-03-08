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

		
$(document).ready(function ()
		  {
	 		
		     $("#selectvideo").submit(function ()
		    		 
		     {	   
		    	 var value =$('#Rvideo option:selected').val();
		         $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/TSelectid",
		        	 data:{value:value},
		        	 async: false,
		        	 success:function(data){
		        		 $("#id_name").html(data);
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
            height: 500px;
            border: 5px solid #EEEEEE;
            background-color: white;
            /*让div水平居中*/
            margin-top: 10px;
            margin:auto;
           
        }
        .id-btn{
			width: 200px;
        	height: 100px;
           /*   border:2px pink solid; */ 
             margin-left:20px;
              margin-top:5px;
             float:left;
		}
        .selectvideo{
        	width: 200px;
            height: 60px;
            margin-top:2px;
            margin-left:0px;
            float:left;
  		/*  border: 2px solid #2daae1;  */
        }
        .mVideo{
        	width: 500px;
            height: 380px;
            margin-left:50px;
            float:left;
          /*    border: 2px solid green;  */
            background:url('video/loading.gif');
            backgroud-size:30px 30px;
            backgroud-repeat:no-repeat; 
    		background-position: center center;
        }
        .myvideo{
        	width: 500px;
            height: 380px;
            margin-left:10px;       
  			/* border: 2px solid black;  */
        }
         select{
        	width: 249px;
        	height: 30px;
        	font-size:18px;
        	text-align:center;
        /* 	border:2px #2daae1 solid; */
        	}
        	.btn{
        	width: 150px;
            height: 50px;
  	      /*   border: 1px solid black;  */
        	}
        #btn_sn{
            width: 80px;
            height: 30px;
            background-color: #2daae1;
      	    border: 1px solid #2daae1;    
            border-radius: 5px;
            margin-left:20px;   
            float:left;
        }
 	 p{
        	font:18px "黑体";
        }
        #id_name{
        width:200px;
        height:100px;
        margin-left:250px;
        margin-top: 380px;
/*         border: 1px solid #2daae1;   */ 
        }
        #Rvideo{
        width:150px;
        height:30px;
        margin:5px;
        } 

    
</style>

<body >
<div class="layout">	
	<div class="myvideo" style="float:left;" >
	<p>行人提取后视频：</p>
	<video width="450" height="350" loop="loop" autoplay="autoplay" controls="controls"style="margin-left:10px;">
	<source src="/output_video/${requestScope.video}/${requestScope.track_vname}" type="video/mp4"></source>
	</video>
	</div>
	<div class="mVideo" id="mVideo"></div>
<form  id="selectvideo" >
		<div class="id-btn">
			<div class="selectvideo">
				<p>选择录入关注人视频：</p>
			
				<select id="Rvideo" name="Rvideo" runat="server" >
					<c:forEach items="${requestScope.vname}" var="item" varStatus="vs">
            			<option value="${item}">${item}</option>
            		</c:forEach>
            	</select>
			</div>
			<div class="btn">
				<input type="submit" id="btn_sn" value="确定">
			</div>
		</div>
		<div id ="id_name"></div>
</form>

</div>	

</body>
</html>