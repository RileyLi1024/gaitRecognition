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




  	  	<!-- Main bar -->
  	<div class="mypicture">
	    <!-- Page heading -->
	   
	    <div class="video1" id="fade_focus" style="float:left;margin-left:75px;margin-right:150px;" >
			   <div class="loading">Loading...<br /><img src="/p/loading3.gif" width="350" height="350" /></div>
			   <h3><font size="+2"><span style="color:blue;">video1:</span></font></h3>
			   <c:forEach items="${requestScope.filename}" var="name" varStatus="vs">
<!-- 			<p class="font-bold text-success">两个视频中的人为同一人</p> -->
			   <ul>
			   <li><img src="video1/${name}" width="400" height="350" /></li>
			   </ul>	
			   </c:forEach>		   		   
	    </div>

        <div class="video2" id="fade" style="position:absolute;left:600px;top:645px" >
			  <div class="loading">Loading...<br /><img src="/p/loading3.gif" width="350" height="350" /></div>
			   <h3><font size="+2"><span style="color:blue;">video2:</span></font></h3>
			   <c:forEach items="${requestScope.filename_two}" var="name_two" varStatus="vs">
 			   <ul> 
 			   <li><img src="video2/${name_two}" width="400" height="350"/></li>
			   </ul>	 
			   </c:forEach>	
	    </div>		 	   		
	    
	     <div class="ending" style="float:left;position:absolute;left:75px;top:1050px;">
	    <form action="resulttwo" method="post">
		<button class="btn btn-sm btn-primary login-submit-cs" type="submit" style="Float:left;width:100px;height:50px"><span style="color:white;">相似性度量</span></button>
		</form>
		</div>
		
		<div style="float:left;position:absolute;left:75px;top:1030px;">
		<h3><span class="text" style="position:absolute;left:370px;width:200px;height:50px">相似度:</span></h3>
		<input type="text" name="相似度" onfocus="this.blur()" value="${requestScope.similarity}" style="position:absolute;left:450px;width:150px;height:25px">
		</div>
		<div style="float:left;position:absolute;left:75px;top:1060px;">
		<h3><span class="text" style="position:absolute;left:300px;width:200px;height:50px">相似性度量结果:</span></h3>
		<input type="text" name="相似度度量结果" onfocus="this.blur()" value="${requestScope.fruit}" style="position:absolute;left:450px;width:150px;height:25px">
	    </div>
	    
	    	 					
		</div>	







</body>
</html>

