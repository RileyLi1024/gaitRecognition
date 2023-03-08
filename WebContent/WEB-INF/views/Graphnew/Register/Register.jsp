<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 
<!DOCTYPE html>
<html lang="en">
 <style>
        *{
            margin: 0px;
            padding: 0px;
            box-sizing: border-box;
        }
        body{
            background: url("image/register_bg.png") no-repeat;
        }
        .rg_layout{
            width: 1200px;
            height: 120px;
            border: 5px solid #EEEEEE;
            background-color: white;
            /*让div水平居中*/
            margin: auto;
           
        }
        .rg_left{
            float: left;
            margin: 15px;
            width: 25%;
        }
        .rg_left > p:first-child{
            color: #FFD026;
            font-size: 20px;
        }
        .rg_left > p:last-child{
            color: #A6A6A6;
        }
        .rg_center{
            /*border: 1px solid red;*/
            float: left;
            width: 500px;
            /*margin: 15px;*/
        }
        .rg_right{
            float: right;
            margin: 15px;
        }
        .rg_right > p:first-child{
            font-size: 15px;
        }
        .rg_right p a {
            color: pink;
        }
        .td_left{
            width: 100px;
            text-align: right;
            height: 45px;
           	font:18px "黑体";
        }
        .td_right{
            padding-left: 10px;
        }
      
        #checkcode{
            width: 110px;
        }
        #img_check{
            height: 32px;
            /*设置垂直居中*/
            vertical-align: middle;
        }
        #btn_sub{
            width: 150px;
            height: 40px;
            background-color: #2daae1;
            border: 1px solid #2daae1;
            margin-left:80px;
            margin-top:8px;
            border-radius: 5px;
            
        }
        .videoReading{  
         width: 1200px;
            height: 470px;
         /*    border: 5px solid red;  */
       /*      background-color: white;  */
            /*让div水平居中*/
             margin: auto;
             margin-top:10px;
        }
    </style>

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
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">

/* 
function confirmEx(){
return confirm("提取行人中，请稍等......");
} */
 
$(document).ready(function ()
		  {
		     
		     $("#vi").submit(function ()
		    		 
		     {	   
		    	 var realpath=$("#f1").val();
		         $.ajax({
		        	 type:'GET',
		        	 url:"<%=request.getContextPath()%>/videoReading",
		        	 data:{f1:realpath},
		        	 async: false,
		        	 success:function(data){
		        		 $("#videoReading").html(data);
		        	 },
		        	 error:function(a){
		        		 alert("出错啦...");
		        	 }	        	 
		         })
		         return false;
		     });    
		 })
		  
	
		
	
</script>


<body >

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
          
          <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>图卷积步态识别方法<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="GraphRegister">关注人录入</a></li>
              <li><a href="GraphTrack">关注人比对</a></li>
    
            </ul>
          </li>  
          
          
          <li class="has_sub"><a href="#"><i class="icon-list-alt"></i>步态识别<span class="pull-right"><i class="icon-chevron-right"></i></span></a>
            <ul>
              <li><a href="showLC">LC-PoseGait方法</a></li>
              <li><a href="show2StreamNet">双流相似度学习方法</a></li>
              <!-- <li><a href="showLSTM">LSTM</a></li>
              <li><a href="showCNN">1D CNN</a></li>
              <li><a href="showLSTM">步态相似度判别</a></li> -->
              <li><a href="showGaitGraph">图卷积步态识别</a></li>
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
	      <h2 class="pull-left"><i class="icon-home"></i>录入</h2>
        <div class="clearfix"></div>
	    </div>
	    <div class="container-fluid">
							<div class="content-error">
								<div class="hpanel">
									<div class="panel-body" >
		<div class="register" runat="server">
		<div class="rg_layout">
        <div class="rg_left">
        </div>
        <div class="rg_center">
            <div class="rg_form">
                <form action="videoReading" method="post" id="vi" enctype="multipart/form-data">
                    <table>                                                                    <tr>
                            <td class="td_left">请导入视频</td>
                            <td class="td_right"><input type="file" placeholder="001.mp4" title="请导入视频1" required="" value="" name="f1" id="f1" class="form-control"></td>
                        </tr>                                                                     					
					   <tr>
                            <td colspan="2" align="center"><input type="submit" id="btn_sub" value="确定" ></td>
                        </tr> 
                        
                        </table>  
                  </form>                  												 
					</div>	 		        		              		
            </div> 
                        
        </div>

          <div class="videoReading" id="videoReading" >
  		        </div>  
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