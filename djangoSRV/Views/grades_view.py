from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context

def get_grades_view(request):
	template = get_template("grades.html")
	grades = __get_student_grades("vv311")
	context = Context( {'name': "Varun Verma",
						'grades' : grades})
	return HttpResponse(template.render(context))	



def __get_student_grades(student_id):
	return [["1", "Variable Assignment", "Addition", 40] ,
			["2", "Conditionals", "If-then-else", 70]
			]