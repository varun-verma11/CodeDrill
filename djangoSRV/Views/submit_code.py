from django.http import HttpResponse
from Forms import SubmitCodeForm
from django.template import Context
import random

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
		if (random.random()>0.5):
			print request
			return HttpResponse("ok")
	return HttpResponse("wrong")