from django.http import HttpResponse, HttpResponseBadRequest
from Forms import SubmitCodeForm
from django.template import Context
import random
import json
from autotester.unit_tester import autotester
from Forms import SubmitCodeForm
from model.models import Test, ModelSolution
from djangoSRV.student import submit_exercise_score,  submit_exercise_code
from StringIO import StringIO
import sys
def submit_student_code(request, ex_id):
	if (request.user.is_authenticated() and request.is_ajax()):
		student_code = request.POST["code"]
                unit_tests= Test.objects.filter(ex_id__exact = ex_id)
                if(not unit_tests.exists()):
                    return HttpResponse("no tests for this exercise")
                test_result = autotester(student_code,
                                         unit_tests[0].test_content)
                # submit result
                final_score = compute_score(test_result)
                print test_result
                print request.user.user_id
                submit_exercise_score(unit_tests[0].ex_id, 
                                request.user,
                                final_score)
                submit_exercise_code(request.user, 
                                unit_tests[0].ex_id, 
                                student_code)

                if no_tests_run(test_result):
                    return HttpResponse("testing did not start")
                if no_errors(test_result) and no_failures(test_result):
                    # at this point it's ok
                    return HttpResponse("ok")                
	return HttpResponse("wrong")

def run_self_test(request):
    if (request.user.is_authenticated() and request.is_ajax()):
        functionCalls = json.loads(request.POST["functionCalls"])
        ex_id = request.POST["ex_id"]
        print ex_id
        code = request.POST["code"]
        model_sollution = ModelSolution.objects.get(ex_id=ex_id).content
        #print model_sollution
        #print code
        #print functionCalls[0]
        ok = True
        for i in range(len(functionCalls)):
            model_code = model_sollution + "\n\n" + "print " + functionCalls[0]
            actual_code = code + "\n\n" + "print " + functionCalls[0]

            try:
                ideal_output = StringIO()
                sys.stdout = ideal_output
                exec model_code
                sys.stdout = sys.__stdout__
            except:
                return HttpResponse("The function has errors")

            try:
                actual_output = StringIO()
                sys.stdout = actual_output
                exec actual_code
                sys.stdout = sys.__stdout__
            except:
                return HttpResponse("Some error has occured:\n\n" + str(sys.exc_info()))

            output = ""
            output += "Expected output:\n"
            output += ideal_output.getvalue() + "\n"
            output += "Actual output:\n"
            output += actual_output.getvalue() + "\n"


            ok = (ideal_output.getvalue() == actual_output.getvalue())
        
        if ok:
            output += "\nTest Passed"
        else:
            output += "\nTest Failed"
        return HttpResponse(output)
    return HttpResponseBadRequest();

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