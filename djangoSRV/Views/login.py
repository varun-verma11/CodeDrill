from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.core.context_processors import csrf
from Forms import LoginForm, StudentRegisterForm, TeacherRegisterForm

def student_login(request):
	login_form = LoginForm()
	reg_form = StudentRegisterForm()
	header = get_template("header.html").render(Context( {'loggedIn':False, 'title':"Student Login"}))
	context = Context({ 'login_form':login_form,
						'register_form' : reg_form,
						'type' : 'student',
						'header':header,
						'title' : 'Student Login',
					});
	try:
		error_text = request.session["error"]
		request.session["error"] = None
		context.update({"error_text": error_text})
	except KeyError:
		None
	context.update(csrf(request))
	template = get_template("login.html");
	return HttpResponse(template.render(context))

def teacher_login(request):
	login_form = LoginForm()
	reg_form = TeacherRegisterForm()
	header = get_template("header.html").render(Context( {'loggedIn':False, 'title':"Teacher Login"}))
	context = Context({ 'login_form':login_form,
						'register_form' : reg_form,
						'type' : 'teacher',
						'header':header,
						'title' : 'Teacher Login'

					});
	context.update(csrf(request))
	try:
		error_text = request.session["error"]
		context.update({"error_text": error_text})
	except KeyError:
		None
	template = get_template("login.html")
	return HttpResponse(template.render(context))
