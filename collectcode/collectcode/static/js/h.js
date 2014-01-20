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
					}else{
						$('#email_error').text(data.msg.e);
						$('#comment_error').text(data.msg.c);
					}					
				}
		})
	})	
})