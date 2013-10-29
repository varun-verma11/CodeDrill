from django.http import HttpResponseRedirect
from Forms import StudentRegisterForm, TeacherRegisterForm
from django.contrib.auth.models import User

def register_student(request):
	form = StudentRegisterForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		email = form.cleaned_data["email"]
		password = form.cleaned_data["password"]
		user = User.objects.create_user(username, email, password)
		if ( user is not None):
			user.last_name = form.cleaned_data["last_name"]
			user.first_name = form.cleaned_data["first_name"]
			user.save();

			#the rest of data needs to go in the manually
			school = form.cleaned_data["school"]
			year = form.cleaned_data["year"]
			Class = form.cleaned_data["Class"]

			return HttpResponseRedirect("/student-login/")
	return HttpResponseRedirect("/student-login/")

def register_teacher(request):
	form = TeacherRegisterForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		email = form.cleaned_data["email"]
		password = form.cleaned_data["password"]
		user = User.objects.create_user(username, email, password)
		if ( user is not None):
			user.last_name = form.cleaned_data["last_name"]
			user.first_name = form.cleaned_data["first_name"]
			user.save()
			#this needs to be put into db
			school = form.cleaned_data["school"]

			return HttpResponseRedirect("/teacher-login/")
	return HttpResponseRedirect("/teacher-login/")
