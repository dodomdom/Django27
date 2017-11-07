$(".comment-reply-button").click(function(event){
			event.preventDefault();
			$(this).parent().next(".comment-reply").fadeToggle();
		})