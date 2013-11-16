from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass, StudentData
from utils import get_header_navbar
from djangoSRV.teacher import get_courses, get_all_exercises


def get_set_exercise_page(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		template = get_template("set_exercise.html")
		teaching_hierarchy = get_courses(request.user.user_id)
		name = request.user.first_name + " " + request.user.last_name
		elements = get_header_navbar("Teacher",name,"Teaching Overview")
		context = Context( {'header' : elements['header'], 
							'menu' : get_template("teacher_menu.html").render(Context({"page":"set_ex"})),
							'teaching_hierarchy' : teaching_hierarchy,
							'navbar' : elements['navbar'],
							'assignment_book' : get_all_exercises()})
		return HttpResponse(template.render(context))
	return HttpResponseRedirect("/")



"""
This is same function as the teacher_view. only difference being the data about students is not required atm. 
Similar structure should be followed for generating pages once the data is retrived from the db
"""
def __get_teaching_hierarchy(teacher_id):
	st_a = StudentData(1, "Variable assignment", "Addition", "Mihai", "50%")
	st_b = StudentData(2, "Conditionals", "If-then-else", "Varun", "100000%")
	st_c = StudentData(3, "Conditionals", "Case", "Rohan", "-10000%")
	students = [st_a, st_b, st_c]

	class_a = TeachingClass("A", students)
	class_b = TeachingClass("B", students)
	class_c = TeachingClass("C", students)

	year_1 = SchoolYear("1", [class_a, class_b, class_c])
	year_2 = SchoolYear("5", [class_b, class_c])

	return TeachingHierarchy([year_1, year_2])