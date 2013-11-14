from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from djangoSRV.student import getStudentAssignments, get_grades, get_number_of_submissions
from utils import get_header_navbar

def student_grades_view(request):
	if request.user.is_authenticated():
		NUMBER_PER_PAGES = 10
		assignments = getStudentAssignments(request.user.user_id)
		# pages = range(1,(get_number_of_submissions(request.user.user_id)/NUMBER_PER_PAGES)+1)
		# if not pages:
		# 	pages = None
		pages = None
		menu = get_template("student_menu.html").render(Context({ 'assignments' : assignments, 'page': 'grades'}))
		elements = get_header_navbar("Student",request.user.first_name + " " + request.user.last_name,"Student Overview")
		context = Context( {'header' : elements['header'],
                            'navbar' : elements['navbar'],
							'menu': menu,
							'pages': pages,
							'grades' : get_grades(request.user.user_id, 1, NUMBER_PER_PAGES)
						})
		context.update(csrf(request))
		template = get_template("student_grades.html")
		return HttpResponse(template.render(context))
	return HttpResponseRedirect('/')
