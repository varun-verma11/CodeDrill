from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from auth import auth_utils
from exercise_data_structure import AssignmentsBook, Chapter, Assignment

def view_spec(request):
	if (request.user.is_authenticated()):
		template = get_template("view_spec.html")
		context = Context(
				{ 'assignment_book': __get_assignments_book()
				})
		return HttpResponse(template.render(context))
	return HttpResponseRedirect("/")

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