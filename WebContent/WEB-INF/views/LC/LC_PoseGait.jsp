<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
	<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%><%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html lang="en">

<script language="javascript" type="text/javascript">
function confirmEx(){
return confirm("提取关节点中，请稍等......");
}




</script>

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <!-- Title and other stuffs -->
  <title>步态识别与相似性度量</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
 <meta name="author" content=""> 
  <!-- Stylesheets -->
  <link href="style/bootstrap.css" rel="stylesheet">
  <!-- Font awesome icon -->
  <link rel="stylesheet" href="style/font-awesome.css"> 
  <!-- jQuery UI -->
  <link rel="stylesheet" href="style/jquery-ui.css"> 
  <!-- Calendar -->
  <link rel="stylesheet" href="style/fullcalendar.css">
  <!-- prettyPhoto -->
  <link rel="stylesheet" href="style/prettyPhoto.css">  
  <!-- Star rating -->
  <link rel="stylesheet" href="style/rateit.css">
  <!-- Date picker -->
  <link rel="stylesheet" href="style/bootstrap-datetimepicker.min.css">
  <!-- CLEditor -->
  <link rel="stylesheet" href="style/jquery.cleditor.css"> 
  <!-- Uniform -->
  <link rel="stylesheet" href="style/uniform.default.css"> 
  <!-- Bootstrap toggle -->
  <link rel="stylesheet" href="style/bootstrap-switch.css">
  <!-- Main stylesheet -->
  <link href="style/style.css" rel="stylesheet">
  <!-- Widgets stylesheet -->
  <link href="style/widgets.css" rel="stylesheet">   
  
  <!-- HTML5 Support for IE -->
  <!--[if lt IE 9]>
  <script src="js/html5shim.js"></script>
  <![endif]-->

  <!-- Favicon -->
  <link rel="shortcut icon" href="img/favicon/favicon.png">
  
 
  
</head>

<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
 <script type="text/javascript">
/*  $(document).ready(function ()
  {
     
     $("#loginForm").submit(function () 
     {
         //$("#myvideo").text("视频应该出现在这里 不知道怎么把form里input的两个值通过这边传到后面去");
         $("#myvideo").load("only_video");
         return false;
     });    
 }) */
 
 $(document).ready(function ()
		  {
		     
		     $("#re").submit(function ()
		    		 
		     {		                 
		         $.ajax({
		        	 type:'POST',
		        	 url:"<%=request.getContextPath()%>/LC_register",	
		        	 async: false,
		        	 success:function(data){
		        	
		        		 $("#re_video").html(data);
		        	 },
		        	 error:function(a){
		        		 alert("出错啦...");
		        	 }	        	 
		         })
		         return false;
		     });    
		 })
		 
 $(document).ready(function ()
		  {
		     
		     $("#dis").submit(function ()
		    		 
		     {		                 
		         $.ajax({
		        	 type:'POST',
		        	 url:"<%=request.getContextPath()%>/distinguish",	
		        	 async: false,
		        	 success:function(data){
		        	
		        		 $("#dis_video").html(data);
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
 #bb{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
            border: 1px solid #2daae1;          
            border-radius: 5px;
            
        }
</style>

<body>
<!-- 加滚动条 -->
<div class="navbar navbar-fixed-top bs-docs-nav" role="banner" style="overflow-y: scroll;border: 1;width: 100%;height: 100%"> 
<!-- Header starts -->
  <header>
          <div class="logo">
            <h2>3D步态识别系统</h2>
          </div>
  </header>
<!-- Header ends -->

<!-- Main content starts -->

<div class="content">
    <div class="sidebar">
        <div class="sidebar-dropdown"><a href="#">导航</a></div>

        <!--- Sidebar navigation -->
        <!-- If the main navigation has sub navigation, then add the class "has_sub" to "li" of main navigation. -->
        <ul id="nav">
          <!-- Main menu with font awesome icon -->
          <li><a href="index.jsp" class="open"><i class="icon-home"></i> 首页</a>
          </li>
       <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>数据管理<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showLSTM">重点人员基本信息管理</a></li>
            </ul>
          </li>  
          
          
          <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>步态建模管理<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showLSTM">步态周期提取</a></li>
              <li><a href="showCNN">数据归一化</a></li>
              <li><a href="showCNN">步态特征建模</a></li>
            </ul>
          </li>  
          
          
           <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>模型管理<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showLSTM">步态特征提取模型管理</a></li>
              <li><a href="showCNN">相似度测量模型管理</a></li>
              <li><a href="showCNN">3D骨架图模型管理</a></li>
            </ul>
          </li>  
          
          <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>图卷积步态识别<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="GraphRegister">关注人录入</a></li>
              <li><a href="GraphTrack">关注人比对</a></li>
    
            </ul>
          </li>  
          
          
          <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>步态识别<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showLC">LC-PoseGait</a></li>
              <li><a href="show2StreamNet">双流相似度学习网络</a></li>
              <!-- <li><a href="showLSTM">LSTM</a></li>
              <li><a href="showCNN">1D CNN</a></li>
              <li><a href="showLSTM">步态相似度判别</a></li> -->
              <li><a href="showGaitGraph">图卷积步态身份识别</a></li>
            </ul>
          </li>  
          
          <li class="has_sub"><a href="#"><i class="icon-file-alt"></i>系统管理<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showTestindex">用户管理</a></li>
              <li><a href="showTestp">权限管理</a></li>
              
            </ul>
          </li> 
                                
          
        </ul>
    </div>


  	  	<!-- Main bar -->
  	<div class="mainbar">
	    <!-- Page heading -->
	    <div class="page-head">
	      <h2 class="pull-left"><i class="icon-home"></i>LC-PoseGait</h2>
        <div class="clearfix"></div>
	    </div>
	    <div class="container-fluid">
							<div class="content-error">
								<div class="hpanel">
									<div class="panel-body" >
																	
									<form action="LC_register" method="post" id="re">
										<button class="btn" id = "bb" type="submit" style="Float:left;width:150px;height:40px;margin-left:35%;"><span style="color:black;font-size:18px;">注 册</span></button>
									</form>	
																					
									<form action="distinguish" method="post" id="dis">
										<button class="btn" id = "bb" type="submit" style="Float:left;width:150px;height:40px;margin-left:20px;"><span style="color:black;font-size:18px;">判 别</span></button>
									</form>	
												
									<div id="re_video" style="clear:both;">
									</div>
									<div id="dis_video" style="clear:both;">
									</div>
										
	
									</div>
									
								</div>
							</div>
						</div>
	    <!-- Page heading ends -->
</div>



<!-- JS -->
<script src="js/jquery.js"></script> <!-- jQuery -->
<script src="js/bootstrap.js"></script> <!-- Bootstrap -->
<script src="js/jquery-ui-1.9.2.custom.min.js"></script> <!-- jQuery UI -->
<script src="js/fullcalendar.min.js"></script> <!-- Full Google Calendar - Calendar -->
<script src="js/jquery.rateit.min.js"></script> <!-- RateIt - Star rating -->
<script src="js/jquery.prettyPhoto.js"></script> <!-- prettyPhoto -->

<!-- jQuery Flot -->
<script src="js/excanvas.min.js"></script>
<script src="js/jquery.flot.js"></script>
<script src="js/jquery.flot.resize.js"></script>
<script src="js/jquery.flot.pie.js"></script>
<script src="js/jquery.flot.stack.js"></script>

<!-- jQuery Notification - Noty -->
<script src="js/jquery.noty.js"></script> <!-- jQuery Notify -->
<script src="js/themes/default.js"></script> <!-- jQuery Notify -->
<script src="js/layouts/bottom.js"></script> <!-- jQuery Notify -->
<script src="js/layouts/topRight.js"></script> <!-- jQuery Notify -->
<script src="js/layouts/top.js"></script> <!-- jQuery Notify -->
<!-- jQuery Notification ends -->

<script src="js/sparklines.js"></script> <!-- Sparklines -->
<script src="js/jquery.cleditor.min.js"></script> <!-- CLEditor -->
<script src="js/bootstrap-datetimepicker.min.js"></script> <!-- Date picker -->
<script src="js/jquery.uniform.min.js"></script> <!-- jQuery Uniform -->
<script src="js/bootstrap-switch.min.js"></script> <!-- Bootstrap Toggle -->
<script src="js/filter.js"></script> <!-- Filter for support page -->
<script src="js/custom.js"></script> <!-- Custom codes -->
<script src="js/charts.js"></script> <!-- Charts & Graphs -->

<!-- Script for this page -->
<script type="text/javascript">
</script>
</div>
</div>
</body>
</html>