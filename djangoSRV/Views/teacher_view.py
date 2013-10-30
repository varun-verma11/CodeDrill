from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
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
    if (request.user.is_authenticated()):
        user = request.user
        teaching_hierarchy = __get_teaching_hierarchy(user.username)
        template = get_template("teacher_view.html")
        context = Context( {'name': user.first_name + " " + user.last_name , 
                            'teaching_hierarchy' : teaching_hierarchy})
        return HttpResponse(template.render(context))
    return HttpResponseRedirect("/")
    

def __get_teaching_hierarchy(teacher_id):
	st_a = StudentData(1, "Variable assignment", "Addition", "Mihai", "50%") #I only get 50% for an addition exercise???
	st_b = StudentData(2, "Conditionals", "If-then-else", "Varun", "100000%")
	st_c = StudentData(3, "Conditionals", "Case", "Rohan", "-10000%")
	students = [st_a, st_b, st_c]

	class_a = TeachingClass("A", students)
	class_b = TeachingClass("B", students)
	class_c = TeachingClass("C", students)

	year_1 = SchoolYear("1", [class_a, class_b, class_c])
	year_2 = SchoolYear("5", [class_b, class_c])

	return TeachingHierarchy([year_1, year_2])



