<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%> 
<!DOCTYPE html>
<html lang="en">


<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta charset="UTF-8">


</head>

<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script type="text/javascript">

/* function confirmEx(){
	return confirm("注册中，请稍等......");
	}
		 */
		

		 
</script>

<body >



 <div class="r">
                <form action="videoReading" method="post" id="vi" enctype="multipart/form-data">
                    <table>                                                                    <tr>
                            <td class="td_left">请导入视频</td>
                            <td class="td_right"><input type="file" placeholder="001.mp4" title="请导入视频1" required="" value="" name="f1" id="f1" class="form-control"></td>
                        </tr>                                                                     					
					   <tr>
                            <td colspan="2" align="center"><input type="submit" id="btn_sub" value="确定" onclick="confirmEx()"></td>
                        </tr> 
                        
                        </table>  
                  </form>                  												 
					</div>	 

	

</body>
</html>