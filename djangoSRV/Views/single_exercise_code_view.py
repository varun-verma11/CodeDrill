from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from djangoSRV.student import get_exercise, getStudentAssignments
from utils import get_header_navbar

def single_exercise_view(request, ex_id):
	if (request.user.is_authenticated()):
		template = get_template("single_exercise.html")
		exercise = get_exercise(ex_id)
		code_form = SubmitCodeForm(initial={'code':exercise[3]},auto_id="id_%s_"+ex_id)
		assignments = getStudentAssignments(request.user.stu_id)
		menu = get_template("student_menu.html").render(Context({ 'assignments' : assignments, 'page':'code'}))
		elements = get_header_navbar("Student",request.user.first_name + " " + request.user.last_name,"Student Overview")
		context = Context( {'menu' : menu,
							'header' : elements['header'],
                            'navbar' : elements['navbar'],
							'description' : exercise[4],
							'ex_id' : ex_id,
							'code_form' : code_form
						})
		context.update(csrf(request))
		return HttpResponse(template.render(context))
	return HttpResponse("Not allowed")