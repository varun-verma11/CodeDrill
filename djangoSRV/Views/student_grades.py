from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment

def student_grades_view(request):
	if request.user.is_authenticated():
		assignments = __get_assignments_book()
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