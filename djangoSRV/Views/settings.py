from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from djangoSRV.student import get_exercise, getStudentAssignments

def teacher_account_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		return HttpResponse(get_template("account_settings_teacher.html").render(Context()))
	return HttpResponseRedirect("/")

def student_account_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Student")):
		return HttpResponse(get_template("account_settings_teacher.html").render(Context()))
	return HttpResponseRedirect("/")

def class_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		return HttpResponse(get_template("class_settings.html").render(Context()))
	return HttpResponseRedirect("/")