from django.http import HttpResponse, HttpResponseRedirect
from Forms import StudentRegisterForm, TeacherRegisterForm

def register_student(request):
	form = StudentRegisterForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		first_name = form.cleaned_data["first_name"]
		last_name = form.cleaned_data["last_name"]
		email = form.cleaned_data["email"]
		school = form.cleaned_data["school"]
		year = form.cleaned_data["year"]
		Class = form.cleaned_data["Class"]
		password = form.cleaned_data["password"]

		return HttpResponse("Registration Successful " + first_name + " " + last_name)
	return HttpResponseRedirect("/student-login/")

def register_teacher(request):
	form = TeacherRegisterForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["username"]
		first_name = form.cleaned_data["first_name"]
		last_name = form.cleaned_data["last_name"]
		email = form.cleaned_data["email"]
		school = form.cleaned_data["school"]
		password = form.cleaned_data["password"]

		return HttpResponse("Registration Successful " + first_name + " " + last_name)
	return HttpResponse("/teacher-login/")
