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
			 	
				     $("#selectid").submit(function ()
				    		 
				     {	 
				    	 var value =$('#Rid option:selected').val();
				         $.ajax({
				        	 type:'GET',
				        	 url:"<%=request.getContextPath()%>/Track_person",
				        	 async: false,
				        	 data:{value:value},
				        	 success:function(data){
				        		 $("#mVideo").html(data);
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
        select{
        	width: 280px;
        	height: 30px;
        	font-size:18px;
        	text-align:center;
        /*  	border:2px #2daae1 solid;  */
        	}
        	.btn1{
        	width: 180px;
            height: 50px;
  	       /*  border: 1px solid red;   */
        	}
        #btn_sn1{
            width: 80px;
            height: 30px;
            background-color: #2daae1;
      	    border: 1px solid #2daae1;  
            border-radius: 5px;
            margin-left:42px; 
            margin-top:7px;  
        }
         p{
    
        	font:18px "黑体";
        	
        }
        #Rid{
        	width:150px;
        	height:30px;
        	margin:5px;
        }
      .id-btn1{
			width: 280px;
        	height: 100px;
           /*   border:2px pink solid;  */
             margin-left:10px;
              margin-top:5px;
             float:left;
		}
	  /* .mVideo{
        	width: 500px;
            height: 380px;
            margin-left:50px;
            float:left;
             border: 2px solid green; 
            background:url('video/loading.gif');
            backgroud-size:30px 30px;
            backgroud-repeat:no-repeat; 
    		background-position: center center;
        } */
		
</style>

<body >

<form id="selectid" action="TResult">
		<div class="id-btn1">
			<div class="selectid">
				<p>选择该视频内已录入关注人id：</p>	
				<select id="Rid" name="Rid" runat="server" >
					<c:forEach items="${requestScope.vid}" var="item" varStatus="vs">
            			<option value="${item}">${item}</option>
            		</c:forEach>
            	</select>
			</div>
			<div class="btn1">
				<input type="submit" id="btn_sn1" value="确定" >
			</div>
		</div>	
</form>

<!-- <div class="mVideo" id="mVideo"></div> -->
</body>
</html>