from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from utils import get_header_navbar
from djangoSRV.teacher import get_courses_with_assignments
from djangoSRV.student import getStudentAssignments


def view_submissions_teacher(request):
	if (request.user.is_authenticated()):
		teaching_hierarchy = get_courses_with_assignments(request.user.user_id)
		menu = get_template("teacher_menu.html").render(Context({'page':'view_sub'}))
		elements = get_header_navbar("Teacher",request.user.first_name + " " + request.user.last_name,"Submit Feedback")
		template = get_template("view_submission_teacher.html")
		context =  Context({ 'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'teaching_hierarchy' : teaching_hierarchy,
                            'menu': menu
                           });
		return HttpResponse(template.render(context));
	return HttpResponseBadRequest()

def view_student_submissions(request):
	if (request.user.is_authenticated()):
		assignments = getStudentAssignments(request.user.user_id)
		menu = get_template("student_menu.html").render(Context({ 'assignments' : assignments, 'page':'view_sub'}))
		elements = get_header_navbar("Teacher",request.user.first_name + " " + request.user.last_name,"Add New Exercise")
		template = get_template("add_new_exercise.html")
		context =  Context({ 'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'menu': menu
                           });
		return HttpResponse(template.render(context));
	return HttpResponseBadRequest()
