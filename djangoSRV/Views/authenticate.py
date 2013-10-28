from django.http import HttpResponse,HttpResponseRedirect
from Forms import LoginForm

def __check_if_valid_login(username, password):
	return True

def __is_user_teacher(username):
	return True

def authenticate_student(request):
	form = LoginForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		return HttpResponseRedirect("/student-view/")
	return HttpResponseRedirect("/student-login/")

def authenticate_teacher(request):
	form = LoginForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		return HttpResponseRedirect("/teacher-view/")
	return HttpResponseRedirect("/teacher-login/")

