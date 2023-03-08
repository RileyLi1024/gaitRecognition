<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Js实现下拉复选功能</title>
</head>
<body>
<span style="width:200px;height:20px;overflow:hidden;">
	<input type="text" id="selectButton" onclick="myclick();" readonly="true" style="width:200px;height:20px;font-size:12px;"></inut>
</span>
 
 
<span id="selectdiv" style="display:none;border:1px solid #A9A9A9;width:200px;overflow-y :scroll;height:65px;background-color:white;font-size:12px; "
		onMouseOver="mousein()" onMouseOut="mouseout()"> 
</span>
 
</body>



<script type="text/javascript">
	
	//下拉框的数据，视讯编号/视讯名称
	var initlist = ['001/点播视讯','002/直播视讯','003/咪咕视讯'];
	
	//多选下拉框所在的div
	var selecteddiv = document.getElementById("selectdiv");
	
	//鼠标是否在【多选下拉框div】上面（如果在div上面，需要控制鼠标的点击事件，不让div隐藏；否则要让该div隐藏）
	var indiv = false;
	
	//模糊查询input
	var fuzzysearchinput = document.getElementById("fuzzysearch");
	
	//选中的视讯类型（需要传到后台的参数）
	var selectedlist = [];
	//选中的视讯名称（展示在前台给业务员看的）
 
	//var selectednamelist = ['点播视讯'];
	var selectednamelist = [];
	
	window.onload = function(){
		
		//动态创建所有的checkbox元素
		for(var i = 0; i < initlist.length; i++){
			var tmpdiv = document.createElement("div");
			var tmpinput = document.createElement("input");
			tmpinput.setAttribute("name","mycheckbox");
			tmpinput.setAttribute("type","checkbox");
			tmpinput.setAttribute("onclick","mycheck(this)");
			tmpinput.setAttribute("value",initlist[i].substr(0,initlist[i].indexOf("/")));
 
			
			var tmptext = document.createTextNode(initlist[i].substr(initlist[i].indexOf("/")+1,initlist[i].length));
			
			tmpdiv.appendChild(tmpinput);
			tmpdiv.appendChild(tmptext);
		//	tmpinput.setAttribute("checked","checked");			
			selecteddiv.appendChild(tmpdiv);
	    			
		}
		
		
		//鼠标点击事件，如果点击在 selectedbutton，或者是在多选框div中的点击事件，不作处理。其他情况的点击事件，将多选空div隐藏
		document.onclick=function(event){
			if(event.target.id=="selectButton" || indiv){
				return;
			}
			selecteddiv.style.display="none";
			document.getElementById("fuzzysearchdiv").style.display="none";
		};
		
		// 设法循环点击 checkbox 使之触发全选   	
		   defaultChecked();
	    
		// 页面加载时 循环遍历 生成初始化默认选择checkbox
		   function defaultChecked(){
		       for(var i = 0; i < initlist.length; i++){
		          //   alert('i======'+i);
		       }
		   }
		   
		
	};
	
	//点击selectButton，展示多选框
	function myclick (){
		//document.getElementById("fuzzysearchdiv").style.display="block";
		selecteddiv.style.display="block";
	}
	
	//鼠标进入多选框的div【selectdiv】
	function mousein(){
		indiv = true;
	}
	
	//鼠标离开多选框的div【selectdiv】
	function  mouseout(){
		indiv = false;
	}
	
	//checkbox的点击事件
	function mycheck(obj){	
	
		if(obj.checked){
			selectedlist.push(obj.value);
			selectednamelist.push(obj.nextSibling.nodeValue);
		}else{
			for(var i = 0; i < selectedlist.length; i++){
				if(selectedlist[i] == obj.value){
					selectedlist.splice(i,1);
					selectednamelist.splice(i,1);
				}
			}
		}
		document.getElementById("selectButton").value=selectednamelist;
	}
	
	//模糊查询
	function myfuzzysearch(){
		var checkboxlist = document.getElementsByName("mycheckbox");
		for(var i = 0; i < checkboxlist.length; i++){
			if(checkboxlist[i].nextSibling.nodeValue.indexOf(fuzzysearchinput.value) == -1){
				checkboxlist[i].parentNode.style.display = "none";
			}else{
				checkboxlist[i].parentNode.style.display = "block";
			}
		}
	}
	
 
</script>
 
</html>