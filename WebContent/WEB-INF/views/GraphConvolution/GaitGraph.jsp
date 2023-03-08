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
		     
		     $("#loginForm").submit(function ()
		    		 
		     {		  
		    	 var f1=$("#f1").val();
		    	 var f2=$("#f2").val();	                
		         $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/val_video_3",
		        	 data:{f1:f1,f2:f2},
		        	 async: false,
		        	 success:function(data){
		        		 alert('提交成功！');
		        		 $("#myvideo").html(data);
		        	 },
		        	 error:function(a){
		        		 alert("出错啦...");
		        	 }
		        
		        	 
		         })
		         return false;
		     });    
		 })
 </script>

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
          
          
          <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>步态识别<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showLSTM">LSTM+CNN</a></li>     
              <li><a href="show2StreamNet">双路相似度学习</a></li>
              <li><a href="showGaitGraph">图卷积</a></li>
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
	      <h2 class="pull-left"><i class="icon-home"></i>步态相似度判别</h2>
        <div class="clearfix"></div>
	    </div>
	    <div class="container-fluid">
							<div class="content-error">
								<div class="hpanel">
									<div class="panel-body">
										<form action="val_video_3" method="post" id="loginForm" enctype="multipart/form-data">
											<div class="form-group1">
												<label class="control-label" for="firstperson">请导入视频1</label>
												<input type="file" placeholder="001.avi" title="请导入视频1"
													required="" value="" name="f1" id="f1"
													class="form-control"> 	
											</div>
											
											<div class="form-group2">
												<label class="control-label" for="secondperson">请导入视频2</label>
												<input type="file" placeholder="002.avi" title="请导入视频2"
													required="" value="" name="f2" id="f2"
													class="form-control"> 												
											</div>	
										<div>
											<button class="btn btn-success btn-block loginbtn" id="btn" type="submit">提取关节点坐标</button>							
										</div>
										</form>
										
										<div id="myvideo">
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