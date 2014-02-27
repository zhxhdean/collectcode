$(function(){
	
	//post comment button
	$('#post_comment').bind('click',function(){
		$('#email_error').text('');
		$('#comment_error').text('');
		$.ajax({
				url:'/comments/add/',
				type:'post',
				data:{
					csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"').val(),
					email:$('#id_email').val(),					
					comment:$('#id_comment').val(),
					blogid:$('input[name="blogid"').val()
					},
				success:function(data){
					if(data.error == '0'){
						$('#email_error').text(data.msg);
						setTimeout(function(){location.reload();},1000); 
					}else{
						$('#email_error').text(data.msg.e);
						$('#comment_error').text(data.msg.c);
					}					
				}
		})
	})	
})


//reply comment
function reply_comment(email){
	$('#id_comment').val('回复:'+email+'\r\n')
	$('#id_comment').textFocus();
}



/**
* 光标放在最后 $("#文本框ID").textFocus();
* 光标放在第二个字符后面 $("#文本框ID").textFocus(2);
*/
(function($){
	$.fn.textFocus=function(v){
		var range,len,v=v===undefined?0:parseInt(v);
		this.each(function(){
			if($.browser.msie){
				range=this.createTextRange();
				v===0?range.collapse(false):range.move("character",v);
				range.select();
			}else{
				len=this.value.length;
				v===0?this.setSelectionRange(len,len):this.setSelectionRange(v,v);
			}
			this.focus();
		});
		return this;
	}
})(jQuery)