from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from djangoSRV.student import getStudentAssignments


def student_grades_view(request):
	if request.user.is_authenticated():
		assignments = getStudentAssignments(request.user.stu_id)
		context = Context( {'name': request.user.first_name + " " + request.user.last_name ,
							'assignments' : assignments,
							'grades' : __get_grades
						})
		context.update(csrf(request))
		template = get_template("student_grades.html")
		return HttpResponse(template.render(context))
	return HttpResponseRedirect('/')

def __get_grades():
	return[[1, "Variable Assignment", "Addition", "40"],
		   [2, "Conditionals", "If-then-else", "70"], 
		   [3, "Loops", "For","93"] 
		  ]