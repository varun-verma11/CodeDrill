from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from auth import auth_utils
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from utils import get_header_navbar
from Forms import SubmitCodeForm
from djangoSRV.student import get_exercise
from djangoSRV.teacher import get_all_exercises
import json

def view_spec(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")) :
		template = get_template("view_spec.html")
		name = request.user.first_name + " " + request.user.last_name
		elements = get_header_navbar("Teacher",name,"View Specification")
		context = Context(
				{ 'header' : elements['header'],
				  'navbar' : elements['navbar'],
				  'menu' : get_template("teacher_menu.html").render(Context({"page":"view_spec"})),
				  'editor' : SubmitCodeForm(),
				  'assignment_book': get_all_exercises()
				})
		return HttpResponse(template.render(context))
	return HttpResponseRedirect("/")

def get_exercise_details(request):
	if (request.user.is_authenticated() and request.is_ajax()):
		ex_id = request.POST["ex_id"]
		exercise_details = get_exercise(ex_id)
		val = exercise_details[3] + "$%$" + exercise_details[4]
		return HttpResponse(val)

	return HttpResponse("Invalid Query to the Server")