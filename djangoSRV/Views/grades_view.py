from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context

def get_grades_view(request):
    if (request.user.is_authenticated()):
		template = get_template("grades.html")
		student_id = request.user.username
		grades = __get_student_grades(student_id)
		exercises = __get_assigned_exercises(student_id)
		terms = __get_terms_for_student(student_id)
		context = Context( {'name': request.user.first_name + " " + request.user.last_name,
							'grades' : grades, 
							'exercises' : exercises,
							'terms': terms})
		return HttpResponse(template.render(context))	


def __get_terms_for_student(student_id):
	terms = []
	for i in range(1,4):
		terms.append(str(i))
	return terms

def __get_student_grades(student_id):
	return [["1", "Variable Assignment", "Addition", 40] ,
			["2", "Conditionals", "If-then-else", 70]
			]

def __get_assigned_exercises(student_id):
	return [["Var Assignment", ["subtraction"] ],
			["Conditionals", ["If-then-else"] ],
			["For Loop",["Print 10 numbers", "Sum an Array"] ]]