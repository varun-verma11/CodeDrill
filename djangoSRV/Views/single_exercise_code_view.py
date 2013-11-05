from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from djangoSRV.student import get_exercise, getStudentAssignments

def single_exercise_view(request, ex_id):
    if (request.user.is_authenticated()):
		template = get_template("single_exercise.html")
		assignments = __get_assignments_book()
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

def __get_assignments_book():

	as1 = Assignment("If", 111)
	as2 = Assignment("If-then-else", 112)
	ch1 = Chapter("Conditionals", [as1, as2])

	as3 = Assignment("Addition", 113)
	as4 = Assignment("Subtraction", 114)
	ch2 = Chapter("Assignment", [as3, as4])

	as5 = Assignment("Print-10-Numbers", 115)
	as6 = Assignment("Sum", 116)
	ch3 = Chapter("Loops", [as5, as6])

	return AssignmentsBook([ch1, ch2, ch3])