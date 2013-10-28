from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment

def single_exercise_view(request, ex_id):
	template = get_template("single_exercise.html")
	assignments = __get_assignments_book()
	code_form = SubmitCodeForm(initial={'code':"if (1==1): \n\t print 2 \n"})
	context = Context( {'name': "Mihai Jiplea",
						'assignments' : assignments,
						'description' : __get_ex_description(ex_id),
						'title' : __get_ex_title(ex_id),
						'ex_id' : ex_id,
						'code_form' : code_form
					})
	context.update(csrf(request))
	return HttpResponse(template.render(context))


def __get_ex_title(ex_id):
	return "Substraction"

def __get_ex_description(ex_id):
	return """
 			Python is a widely used general-purpose, high-level programming 
 			language.[11][12][13] Its design philosophy emphasizes code 
 			readability, and its syntax allows programmers to express 
 			concepts in fewer lines of code than would be possible in 
 			languages such as C.[14][15] The language provides constructs 
 			intended to enable clear programs on both a small and large 
 			scale.[16] Python supports multiple programming paradigms,
 			including object-oriented, imperative and functional 
 			programming or procedural styles. It features a dynamic 
 			type system and automatic memory management and has a large 
 			and comprehensive standard library
			"""

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