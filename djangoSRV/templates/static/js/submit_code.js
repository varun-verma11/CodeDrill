function submit_code(ex_id) {
  var csrftoken = getCsrfToken();
  alert("start");
  $.ajax({
        type: 'POST',
        url: '/submit-code/'+ex_id+"/",
        data: {
                'code': $('#id_code_'+ex_id).val()
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
                alert("done");
              }
    });
  return false;
}
