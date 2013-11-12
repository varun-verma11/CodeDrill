from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from djangoSRV.student import get_exercise, getStudentAssignments
from utils import get_header_navbar

def teacher_account_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		name = request.user.first_name + " " + request.user.last_name
        elements = get_header_navbar("Teacher",name,"Account Settings")
        context = Context( { 
			        		'menu' : get_template("teacher_menu.html").render(Context()),
			        		'header' : elements['header'],
                            'navbar' : elements['navbar']
		        	})
        settings_page = get_template("account_settings_teacher.html").render(context)
        return HttpResponse(settings_page)
	return HttpResponseRedirect("/")

def student_account_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Student")):
		name = request.user.first_name + " " + request.user.last_name
        elements = get_header_navbar("Student",name,"Account Settings")
        context = Context( { 
			        		'menu' : get_template("teacher_menu.html").render(Context()),
			        		'header' : elements['header'],
                            'navbar' : elements['navbar']
		        	})
        return HttpResponse(get_template("account_settings_student.html").render(context))
	return HttpResponseRedirect("/")

def class_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		name = request.user.first_name + " " + request.user.last_name
        elements = get_header_navbar("Teacher",name,"Class Settings")
        context = Context( { 
			        		'menu' : get_template("teacher_menu.html").render(Context()),
			        		'header' : elements['header'],
                            'navbar' : elements['navbar']
		        	})
        return HttpResponse(get_template("class_settings.html").render(context))
	return HttpResponseRedirect("/")

def change_password(request):
	if (request.user.is_authenticated()):
		new_pw = request.POST["password"]
		old_pw = request.POST["old_password"]
		request.user.password = new_pw
		return HttpResponse("yes")
	return HttpResponse("no")

def change_email(request):
	if (request.user.is_authenticated()):
		new_email = request.POST["email"]

		return HttpResponse("yes")
	return HttpResponse("no")
