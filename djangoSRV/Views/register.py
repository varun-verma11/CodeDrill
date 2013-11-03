from django.http import HttpResponseRedirect
from Forms import StudentRegisterForm, TeacherRegisterForm
from model.models import Student, Teacher
def register_student(request):
	form = StudentRegisterForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["reg_username"]
		email = form.cleaned_data["email"]
		password = form.cleaned_data["reg_password"]
		#user = User.objects.create_user(username, email, password)
		#if ( user is not None):
		last_name = form.cleaned_data["last_name"]
		first_name = form.cleaned_data["first_name"]
		user = Student(uname=username,first_name=first_name, last_name = last_name, pw = password, email = email)
		#g.user_set.add(user)
		user.save();
		#the rest of data needs to go in the manually
		#school = form.cleaned_data["school"]
		#year = form.cleaned_data["year"]
		#Class = form.cleaned_data["Class"]

	return HttpResponseRedirect("/student-login/")
#	return HttpResponseRedirect("/student-login/")

def register_teacher(request):
	form = TeacherRegisterForm(request.POST)
	if (form.is_valid()):
		username = form.cleaned_data["reg_username"]
		email = form.cleaned_data["email"]
		password = form.cleaned_data["reg_password"]
		
		#if ( user is not None):
		last_name = form.cleaned_data["last_name"]
		first_name = form.cleaned_data["first_name"]
		user = Teacher(uname=username, first_name=first_name, last_name=last_name, email=email, pw=password)
                #g = Group.objects.get(name='Teacher')
		#g.user_set.add(user)
		user.save()
		#this needs to be put into db
		#school = form.cleaned_data["school"]

	return HttpResponseRedirect("/teacher-login/")
