from django.http import HttpResponseRedirect, HttpResponse
from Forms import LoginForm
from django.contrib.auth import authenticate, login
from model.models import Student, Teacher


def authenticate_student(request):
	form = LoginForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		user = authenticate(username=username, password=password,
			token="student") #token is the additional option
		if (user is not None):
			user.backend = "djangoSRV.login.student_auth.StudentBackend"
			login(request, user)
			return HttpResponseRedirect("/student-view/")
	request.session["error"] = 'Wrong username/password'
	return HttpResponseRedirect("/student-login/")

def authenticate_teacher(request):
	form = LoginForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		print username, password
		user = authenticate(username=username, password=password, token="teacher") #token is the additional option
		if (user is not None):
			user.backend = "djangoSRV.login.teacher_auth.TeacherBackend"
			login(request, user)
			return HttpResponseRedirect("/teacher-view/")
		return HttpResponseRedirect("/teacher-login/")
	request.session["error"] = 'Wrong username/password '
	return HttpResponseRedirect("/teacher-login/")


def check_user_name_exists(request):
	if (request.is_ajax()):
		username = request.POST["username"]
		if (Student.objects.filter(uname=username).count()):
			return HttpResponse("yes")
		return HttpResponse("no")
	return HttpResponse("invalid query")

