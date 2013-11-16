function check_username_exists()
{
	var csrftoken = getCsrfToken();
	$.ajax({
	        type: 'POST',
	        url: '/check-username/',
	        data: {
	                'username': user.val()
	              },
	        beforeSend: function(xhr, settings) 
	              {
	                xhr.setRequestHeader("X-CSRFToken", csrftoken);
	              },
	        success: function(response) 
	              {
	                if(response=="yes")
	                {
	                	return true;
	                } else if (response=="no")
	                {
	                 return false;
	                }
	              }
	    });
	return false;
}