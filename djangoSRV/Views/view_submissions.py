from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from utils import get_header_navbar
import json
from djangoSRV.teacher import get_courses_with_assignments2
from djangoSRV.student import getStudentAssignments, getStudentAssignments, submit_feedback_for_student, get_feedback_for_student


def view_submissions_teacher(request):
	if (request.user.is_authenticated()):
		teaching_hierarchy = get_courses_with_assignments2(request.user.user_id) #variant to see how this works
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
		elements = get_header_navbar("Student",request.user.first_name + " " + request.user.last_name,"Add New Exercise")
		template = get_template("view_submission_student.html")
		context =  Context({ 'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'menu': menu,
                            'assignments' : getStudentAssignments(request.user.user_id)
                           });
		return HttpResponse(template.render(context));
	return HttpResponseBadRequest()

def get_student_feedback(request,ex_id):
	if (request.user.is_authenticated() and request.is_ajax()):
		print request.user.user_id, ex_id
		return HttpResponse(json.dumps([get_feedback_for_student(ex_id, request.user.user_id)]))
	return HttpResponseBadRequest()

def submit_student_feedback(request):
	if (request.user.is_authenticated() and request.is_ajax()):
		std_id = request.POST['stu_id']
		ex_id  = request.POST['ex_id']
		feedback = request.POST['feedback']
		if (submit_feedback_for_student(std_id, request.user.user_id, ex_id,feedback)):
			return HttpResponse("")
	return HttpResponseBadRequest()
