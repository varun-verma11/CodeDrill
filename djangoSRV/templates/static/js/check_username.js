function check_username()
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
	                  //display wrong username a cross
	                  alert("username is fine")
	                } else if (response=="no")
	                {
	                	alert("change username")
	                  //display usrname is correct possibly with a tick
	                }
	              }
	    });
	return false;
}