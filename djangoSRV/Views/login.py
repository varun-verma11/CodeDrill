from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.core.context_processors import csrf
from Forms import LoginForm, StudentRegisterForm, TeacherRegisterForm

def student_login(request):
	login_form = LoginForm()
	reg_form = StudentRegisterForm()
	context = Context({ 'login_form':login_form,
						'register_form' : reg_form,
						'type' : 'student',
						'title' : 'Student Login'
					});
	context.update(csrf(request))
	template = get_template("login.html");
	return HttpResponse(template.render(context))

def teacher_login(request):
	login_form = LoginForm()
	reg_form = TeacherRegisterForm()
	context = Context({ 'login_form':login_form,
						'register_form' : reg_form,
						'type' : 'teacher',
						'title' : 'Teacher Login'

					});
	context.update(csrf(request))
	template = get_template("login.html")
	return HttpResponse(template.render(context))
