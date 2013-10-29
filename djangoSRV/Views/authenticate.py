from django.http import HttpResponseRedirect
from Forms import LoginForm
from django.contrib.auth import authenticate, login

def authenticate_student(request):
	form = LoginForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		user = authenticate(username=username, password=password)
		if (user is not None):
			if (user.is_active and user.groups.filter(name="Student").exists()):
				login(request, user)
				return HttpResponseRedirect("/student-view/")
	return HttpResponseRedirect("/student-login/")

def authenticate_teacher(request):
	form = LoginForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		password = form.cleaned_data["password"]
		user = authenticate(username=username, password=password)
		if (user is not None):
			if (user.is_active and user.groups.filter(name="Teacher").exists()):
				login(request, user)
				return HttpResponseRedirect("/teacher-view/")
	return HttpResponseRedirect("/teacher-login/")

