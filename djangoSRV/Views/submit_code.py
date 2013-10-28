from django.http import HttpResponse
from Forms import SubmitCodeForm
from django.template import Context

def submit_student_code(request, ex_id):
	form = SubmitCodeForm(request.POST)
	if (form.is_valid()):
		code = form.cleaned_data["code"]

		"""
			****************************
			****************************
				 CODE TO TEST THE 
			    SUBMITTED CODE GOES 
					   HERE
			****************************
			****************************

		"""
		return HttpResponse("Code Submitted for ex id: " + ex_id + "<br>" + code)
	return HttpResponse("ERROR")