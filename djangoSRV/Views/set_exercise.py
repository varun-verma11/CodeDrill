from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass, StudentData

def get_set_exercise_page(request):
	template = get_template("set_exercise.html")
	teacher_id = "mmj211"
	teaching_hierarchy = __get_teaching_hierarchy(teacher_id)
	assignment_book = __get_assignments_book()
	
	context = Context( {'name': "Mihai Jiplea", 
						'teaching_hierarchy' : teaching_hierarchy,
						'assignment_book' : assignment_book})

	return HttpResponse(template.render(context))


def __get_assignments_book():
	as1 = Assignment("If", 111)
	as2 = Assignment("If-then-else", 123)
	ch1 = Chapter("Conditionals", [as1, as2])

	as3 = Assignment("Addition", 145)
	as4 = Assignment("Subtraction", 143)
	ch2 = Chapter("Assignment", [as3, as4])

	as5 = Assignment("Print 10 Numbers", 154)
	as6 = Assignment("Sum", 143)
	ch3 = Chapter("Loops", [as5, as6])

	return AssignmentsBook([ch1, ch2, ch3])



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