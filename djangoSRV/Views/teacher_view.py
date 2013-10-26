from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseForbidden
from django.template import Context
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass, StudentData
from auth import auth_utils
from exercises.models import Teacher, Course 

def get_teacher_view(request):
    # if not auth_utils.is_authenticated_session(request.session):
    #     return redirect_to_login(request)
    # if not has_permission(request.session):
    #     return HttpResponseForbidden

    # at this point it should be a guaranteed that the session has
    # a key named 'user_id' representing a teacher

    teacher_id = "mmj211"
    return get_teacher_view_with_username(teacher_id)
    

    # teaching_hierarchy = __get_teaching_hierarchy(request.session['user_id'])
    
def get_teacher_view_with_username(teacher_id):
    teaching_hierarchy = __get_teaching_hierarchy(teacher_id)
    template = get_template("teacher_view.html")
    context = Context( {'name': "Mihai Jiplea", 
                        'teaching_hierarchy' : teaching_hierarchy})
    return HttpResponse(template.render(context))


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


