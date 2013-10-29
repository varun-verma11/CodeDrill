from django.http import HttpResponse
from Forms import SubmitCodeForm
from django.template import Context
import json

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
	return HttpResponse(json.dumps({'grade':'ok'}), content_type='application/json')