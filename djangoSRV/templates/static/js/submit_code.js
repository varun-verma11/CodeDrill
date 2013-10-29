function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function submit_code(ex_id) {
  var csrftoken = getCookie('csrftoken');
  $.ajax({
        type: 'POST',
        url: '/submit-code/'+ex_id+"/",
        data: {
                'code': $('id_code_'+ex_id).val()
              },
        beforeSend: function(xhr, settings) 
              {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
              },
        success: function(response) 
              {
                if(response=="ok")
                {
                  $('#wrong_'+ex_id).hide();
                  $('#ok_'+ex_id).show();
                } else 
                {
                  $('#ok_'+ex_id).hide();
                  $('#wrong_'+ex_id).show();
                }
              }
    });
  return false;
}
