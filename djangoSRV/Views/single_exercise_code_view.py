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
		assignments = getStudentAssignments(request.user.stu_id)
		menu = get_template("student_menu.html").render(Context({ 'assignments' : assignments}))
		header = get_template("header.html").render(
                    Context( {
                        'type': 'Student', 
                        'name': request.user.first_name + " " + request.user.last_name,
                        'title': "Single Exercise"  ,
                        'loggedIn':True} ))
		context = Context( {'menu' : menu,
							'header' : header,
							'description' : exercise[4],
							'ex_id' : ex_id,
							'code_form' : code_form
						})
		context.update(csrf(request))
		return HttpResponse(template.render(context))