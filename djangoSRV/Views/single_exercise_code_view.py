from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from djangoSRV.student import get_exercise, getStudentAssignments

def single_exercise_view(request, ex_id):
    if (request.user.is_authenticated()):
		template = get_template("single_exercise.html")
		exercise = get_exercise(ex_id)
		code_form = SubmitCodeForm(initial={'code':exercise[3]},auto_id="id_%s_"+ex_id)
		name = request.user.first_name + " " + request.user.last_name
		ass_b = getStudentAssignments(request.user.stu_id)
		context = Context( {'assignments' : ass_b,
							'description' : exercise[4],
							'title' : name + " | " + exercise[1],
							'ex_id' : ex_id,
							'code_form' : code_form
						})
		context.update(csrf(request))
		return HttpResponse(template.render(context))