from django.http import HttpResponse
from Forms import SubmitCodeForm
from django.template import Context
import random
from tester import autotester
from Forms import SubmitCodeForm

def submit_student_code(request, ex_id):
	# form = SubmitCodeForm(request.POST)
	# if (form.is_valid()):
	# 	code = form.cleaned_data["code"]

	# 	"""
	# 		****************************
	# 		****************************
	# 			 CODE TO TEST THE 
	# 		    SUBMITTED CODE GOES 
	# 				   HERE
	# 		****************************
	# 		****************************

	# 	"""
	# 	print "returning value now"
	# 	return HttpResponse("k")
	if (request.user.is_authenticated() and request.is_ajax()):
		print request
		student_code = request.POST["code"]
		test_code = ""
		if (autotester (student_code, test_code)):
			return HttpResponse("ok")
	return HttpResponse("wrong")