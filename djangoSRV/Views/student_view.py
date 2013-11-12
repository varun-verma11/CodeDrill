from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from model.models import AssignedExercises, Student, Course, Exercise
from djangoSRV.student import get_exercise, getStudentAssignments
from utils import get_header_navbar


def get_student_view(request):
    if (request.user.is_type("Student")):
        assignments = __get_assignments_book(request.user.stu_id)
        menu = get_template("student_menu.html").render(Context({ 'assignments' : assignments, 'page':'code'}))
        elements = get_header_navbar("Student",request.user.first_name + " " + request.user.last_name,"Student Overview")
        context = Context({ 'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'menu': menu,
                            'form':SubmitCodeForm(),
                            'assignments' : assignments
                        })
        context.update(csrf(request))
        template = get_template("student_home.html")
        return HttpResponse(template.render(context))
    return HttpResponseRedirect("/")

def __get_assignments_book(uid):
    assignment_book = getStudentAssignments(uid)
    for chapter in assignment_book.get_chapters():
        for assignment in chapter.get_assignments():
            assignment.set_code(SubmitCodeForm(initial={'code':get_exercise(assignment.get_id)[3]},auto_id="id_%s_"+str(assignment.get_id())))


    return assignment_book

