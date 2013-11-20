from django.http import HttpResponse
from Forms import SubmitCodeForm
from django.template import Context
import random
from autotester.unit_tester import autotester
from Forms import SubmitCodeForm
from model.models import Test
from djangoSRV.student import submit_exercise

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
		student_code = request.POST["code"]
		# test_code = ""
                unit_tests= Test.objects.filter(ex_id__exact = ex_id)
                if(not unit_tests.exists()):
                    return HttpResponse("no tests for this exercise")
		# if (autotester (student_code, test_code)):
		#     return HttpResponse("ok")
                test_result = autotester(student_code,
                                         unit_tests[0].test_content)
                # submit result
                final_score = compute_score(test_result)
                print test_result
                print request.user.user_id
                submit_exercise(unit_tests[0].ex_id, 
                                request.user,
                                final_score)
                if no_tests_run(test_result):
                    return HttpResponse("testing did not start")
                if no_errors(test_result) and no_failures(test_result):
                    # at this point it's ok
                    return HttpResponse("ok")                
	return HttpResponse("wrong")


# see if there were any tests run by the autotester
def no_tests_run(test_result):
    return test_result[2] is 0

# check if there were no errors or failures
def no_errors(test_result):
    return test_result[0] is 0

def no_failures(test_result):
    return test_result[1] is 0
  
# compute the score for submission in the DB from a test_result
#30% for compilation,
# the rest proportional to successful tests
def compute_score(test_result):
    if no_tests_run(test_result):
        return 0
    return (test_result[2] - test_result[1] - test_result[0])*100/test_result[2]