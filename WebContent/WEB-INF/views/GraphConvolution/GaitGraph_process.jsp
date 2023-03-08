<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
	<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%><%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html lang="en">


<script language="javascript" type="text/javascript">
/*
by: /
*/
//主函数
//video1
function s()
{
var interv=1000; //切换时间
var interv2=10; //切换速速
var opac1=80; //文字背景的透明度
var source="fade_focus" //图片容器的id名称
//获取对象
function getTag(tag,obj)
{if(obj==null)
   {return document.getElementsByTagName(tag)}
 else
 {return obj.getElementsByTagName(tag)}}
 
function getid(id)
{return document.getElementById(id)};

var opac=0,j=0,t=63,num,scton=0,timer,timer2,timer3;var id=getid(source);id.removeChild(getTag("div",id)[0]);var li=getTag("li",id);var div=document.createElement("div");var title=document.createElement("div");var span=document.createElement("span");var button=document.createElement("div");button.className="button";
    for(var i=0;i<li.length;i++)
    {var a=document.createElement("a");
    a.innerHTML=i+1;a.onclick=function(){clearTimeout(timer);clearTimeout(timer2);clearTimeout(timer3);j=parseInt(this.innerHTML)-1;scton=0;t=63;opac=0;fadeon();};
    a.className="b1";a.onmouseover=function(){this.className="b2"};a.onmouseout=function(){this.className="b1";sc(j)};button.appendChild(a);}
//控制图层透明度
function alpha(obj,n){if(document.all){obj.style.filter="alpha(opacity="+n+")";}else{obj.style.opacity=(n/100);}}
//控制焦点按钮
function sc(n){for(var i=0;i<li.length;i++){button.childNodes[i].className="b1"};button.childNodes[n].className="b2";}
title.className="num_list";
title.appendChild(span);
alpha(title,opac1);
id.className="d1";
div.className="d2";
id.appendChild(div);
id.appendChild(title);
//id.appendChild(button);
 //渐显
 var fadeon=function(){opac+=5;div.innerHTML=li[j].innerHTML;span.innerHTML=getTag("img",li[j])[0].alt;alpha(div,opac);if(scton==0){sc(j);num=-2;scrolltxt();scton=1};if(opac<100){timer=setTimeout(fadeon,interv2)}else{timer2=setTimeout(fadeout,interv);};}
//渐隐 这边初始幻灯片是 opac>0
 var fadeout=function(){opac-=5;div.innerHTML=li[j].innerHTML;alpha(div,opac);if(scton==0){num=2;scrolltxt();scton=1};if(opac>100){timer=setTimeout(fadeout,interv2)}else{if(j<li.length-1){j++}else{j=0};fadeon()};}
//滚动文字
 var scrolltxt=function(){t+=num;span.style.marginTop=t+"px";if(num<0&&t>3){timer3=setTimeout(scrolltxt,interv2)}else if(num>0&&t<62){timer3=setTimeout(scrolltxt,interv2)}else{scton=0}};
fadeon();
}

//video2
function t()
{
var interv=1000; //切换时间
var interv2=10; //切换速速
var opac1=80; //文字背景的透明度
var source="fade" //图片容器的id名称
//获取对象
function getTag(tag,obj)
{if(obj==null)
   {return document.getElementsByTagName(tag)}
 else
 {return obj.getElementsByTagName(tag)}}
 
function getid(id)
{return document.getElementById(id)};

var opac=0,j=0,t=63,num,scton=0,timer,timer2,timer3;var id=getid(source);id.removeChild(getTag("div",id)[0]);var li=getTag("li",id);var div=document.createElement("div");var title=document.createElement("div");var span=document.createElement("span");var button=document.createElement("div");button.className="button";
    for(var i=0;i<li.length;i++)
    {var a=document.createElement("a");
    a.innerHTML=i+1;a.onclick=function(){clearTimeout(timer);clearTimeout(timer2);clearTimeout(timer3);j=parseInt(this.innerHTML)-1;scton=0;t=63;opac=0;fadeon();};
    a.className="b1";a.onmouseover=function(){this.className="b2"};a.onmouseout=function(){this.className="b1";sc(j)};button.appendChild(a);}
//控制图层透明度
function alpha(obj,n){if(document.all){obj.style.filter="alpha(opacity="+n+")";}else{obj.style.opacity=(n/100);}}
//控制焦点按钮
function sc(n){for(var i=0;i<li.length;i++){button.childNodes[i].className="b1"};button.childNodes[n].className="b2";}
title.className="num_list";
title.appendChild(span);
alpha(title,opac1);
id.className="d1";
div.className="d2";
id.appendChild(div);
id.appendChild(title);
//id.appendChild(button);
 //渐显
 var fadeon=function(){opac+=5;div.innerHTML=li[j].innerHTML;span.innerHTML=getTag("img",li[j])[0].alt;alpha(div,opac);if(scton==0){sc(j);num=-2;scrolltxt();scton=1};if(opac<100){timer=setTimeout(fadeon,interv2)}else{timer2=setTimeout(fadeout,interv);};}
//渐隐 这边初始幻灯片是 opac>0
 var fadeout=function(){opac-=5;div.innerHTML=li[j].innerHTML;alpha(div,opac);if(scton==0){num=2;scrolltxt();scton=1};if(opac>90){timer=setTimeout(fadeout,interv2)}else{if(j<li.length-1){j++}else{j=0};fadeon()};}
//滚动文字
 var scrolltxt=function(){t+=num;span.style.marginTop=t+"px";if(num<0&&t>3){timer3=setTimeout(scrolltxt,interv2)}else if(num>0&&t<62){timer3=setTimeout(scrolltxt,interv2)}else{scton=0}};
fadeon();
}

//初始化
window.onload=function(){
	s();
	t();
}

</script>




<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <!-- Title and other stuffs -->
  <title>3D步态识别系统</title>
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
  

  
  <style type="text/css" media="all">
.d1{width:400px;height:auto;overflow:hidden;border:#666666 2px solid;background-color:#1E90FF;position:relative;}
.loading{width:400px;border:#666666 2px solid;background-color:#000000;color:#FFCC00;font-size:12px;height:350px;text-align:center;padding-top:30px;font-family:Verdana, Arial, Helvetica, sans-serif;font-weight:bold;}
.d2{width:100%;height:350px;overflow:hidden;} 
/* .num_list{position:absolute;width:100%;left:0px;bottom:-1px;background-color:#000000;color:#FFFFFF;font-size:12px;padding:4px 0px;height:20px;overflow:hidden;} */
/* .num_list span{display:inline-block;height:16px;padding-left:6px;} */
img{border:0px;}
ul{display:none;}
/* .button{position:absolute; z-index:1000; right:0px; bottom:2px; font-size:13px; font-weight:bold; font-family:Arial, Helvetica, sans-serif;} */
/* .b1,.b2{background-color:#666666;display:block;float:left;padding:2px 6px;margin-right:3px;color:#FFFFFF;text-decoration:none;cursor:pointer;} */
/* .b2{color:#FFCC33;background-color:#FF6633;} */

  
/*   	div img{ */
/*   		border:solid 5px #CCBBFF; */
/*   	} */
  </style>
  
</head>

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
          </li> 
                                
          
        </ul>
    </div>


  	  	<!-- Main bar -->
  	<div class="mainbar">
	    <!-- Page heading -->
	    <div class="page-head">
	      <h2 class="pull-left"><i class="icon-home"></i>步态相似度分析</h2>
        <div class="clearfix"></div>
	    </div>
	    <div class="video1" id="fade_focus" style="float:left;margin-left:75px;margin-right:150px;" >
			   <div class="loading">Loading...<br /><img src="/p/loading3.gif" width="350" height="350" /></div>
			   <h3><font size="+2"><span style="color:white;">video1:</span></font></h3>
			   <c:forEach items="${requestScope.filename}" var="name" varStatus="vs">
<!-- 			<p class="font-bold text-success">两个视频中的人为同一人</p> -->
			   <ul>
			   <li><img src="/v1/${name}" width="400" height="350"/></li>
			   </ul>	
			   </c:forEach>		   		   
	    </div>

        <div class="video2" id="fade" style="position:absolute;left:600px;top:60px" >
			  <div class="loading">Loading...<br /><img src="/p/loading3.gif" width="350" height="350" /></div>
			   <h3><font size="+2"><span style="color:white;">video2:</span></font></h3>
			   <c:forEach items="${requestScope.filename_two}" var="name_two" varStatus="vs">
 			   <ul> 
 			   <li><img src="/v2/${name_two}" width="400" height="350"/></li>
			   </ul>	 
			   </c:forEach>	
			  
	    </div>		 	   		
	    
	     <div class="ending" style="float:left;position:absolute;left:75px;top:480px;">
	    <form action="GaitGraph_result" method="post">
		<button class="btn btn-sm btn-primary login-submit-cs" type="submit" style="Float:left;width:100px;height:50px"><span style="color:white;">相似性度量</span></button>
		</form>
		</div>
		
		<div style="float:left;position:absolute;left:75px;top:480px;">
		<h3><span class="text" style="position:absolute;left:370px;width:200px;height:50px">相似度:</span></h3>
		<input type="text" name="相似度" onfocus="this.blur()" value="${requestScope.similarity}" style="position:absolute;left:450px;width:150px;height:25px">
		</div>
		<div style="float:left;position:absolute;left:75px;top:520px;">
		<h3><span class="text" style="position:absolute;left:300px;width:200px;height:50px">相似性度量结果:</span></h3>
		<input type="text" name="相似度度量结果" onfocus="this.blur()" value="${requestScope.fruit}" style="position:absolute;left:450px;width:150px;height:25px">

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


</body>
</html>

