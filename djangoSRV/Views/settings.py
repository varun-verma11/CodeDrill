from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from djangoSRV.student import get_exercise, getStudentAssignments
from utils import get_header_navbar
from acc_queries import *
import json
from djangoSRV.teacher import get_courses, get_students_in_course, add_new_course


def teacher_account_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		name = request.user.first_name + " " + request.user.last_name
        elements = get_header_navbar("Teacher",name,"Account Settings")
        context = Context( { 
			        		'menu' : get_template("teacher_menu.html").render(Context()),
			        		'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'id' : request.user.user_id,
                            'type': 'teacher'
		        	})
        settings_page = get_template("account_settings.html").render(context)
        return HttpResponse(settings_page)
	return HttpResponseRedirect("/")

def student_account_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Student")):
		name = request.user.first_name + " " + request.user.last_name
        elements = get_header_navbar("Student",name,"Account Settings")
        context = Context( { 
			        		'menu' : get_template("student_menu.html").render(Context({ 'assignments' : getStudentAssignments(request.user.user_id)})),
			        		'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'id' : request.user.user_id,
                            'type': 'student'
		        	})
        return HttpResponse(get_template("account_settings.html").render(context))
	return HttpResponseRedirect("/")

def class_settings(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		name = request.user.first_name + " " + request.user.last_name
        elements = get_header_navbar("Teacher",name,"Class Settings")
        context = Context( { 
			        		'menu' : get_template("teacher_menu.html").render(Context()),
			        		'header' : elements['header'],
			        		'teaching_hierarchy': get_courses(request.user.user_id),
                            'navbar' : elements['navbar'],
                            'years' : range(1,13) #should be added later from DB
		        	})
        return HttpResponse(get_template("class_settings.html").render(context))
	return HttpResponseRedirect("/")

def get_registered_students_in_course(request):
	if (request.user.is_authenticated() and request.is_ajax()):
		course_id = request.POST["course_id"]
		students = get_students_in_course(course_id)
		return HttpResponse(json.dumps(students))
	return HttpResponseBadRequest()

def add_new_class(request):
	if (request.user.is_authenticated() and request.is_ajax()):
		course_name = request.POST["name"]
		course_year = request.POST["year"]
		if add_new_course(course_name, int(course_year)):
			return HttpResponse("added")

	return HttpResponseBadRequest()

def change_password(request):
	if (request.user.is_authenticated()):
		new_pw = request.POST["password"]
		old_pw = request.POST["old_password"]
		uid = request.POST['id']
		user_type = request.POST['type']
		if update_password(old_pw, new_pw, uid, user_type):
			return HttpResponse("yes")
		return HttpResponse("no")
	return HttpResponse("no")

def change_email(request):
    if (request.user.is_authenticated()):
        new_email = request.POST["email"]
        uid = request.POST['id']
        user_type = request.POST['type']
        update_email(new_email, uid, user_type)
        return HttpResponse("yes")
    return HttpResponse("no")
