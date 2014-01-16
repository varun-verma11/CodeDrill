from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Context
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from utils import get_header_navbar
import json
from djangoSRV.teacher import get_average_for_all_assignments, get_average_grade_for_year, get_average_grade_for_class, get_student_grades_for_assingments, get_courses_with_assignments2

#from auth import auth_utils
#from model.models import Teacher, Course 

def get_teacher_view(request):

    # at this point it should be a guaranteed that the session has
    # a key named 'user_id' representing a teacher
    if (request.user.is_authenticated() and request.user.is_type("Teacher")):
        name = request.user.first_name + " " + request.user.last_name
        teaching_hierarchy = get_courses_with_assignments2(request.user.user_id)
        template = get_template("teacher_view.html")
        elements = get_header_navbar("Teacher",name,"Teaching Overview")
        context = Context( {'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'teaching_hierarchy': teaching_hierarchy,
                            'menu' : get_template("teacher_menu.html").render(Context({"page":"overview"})),
                            })
        return HttpResponse(template.render(context))
    return HttpResponseRedirect("/")


def get_overview(request):
    if (request.user.is_authenticated() and request.is_ajax()):
        tch_id = request.user.user_id
        table = get_average_for_all_assignments(tch_id)
        return HttpResponse(json.dumps(table))
    return HttpResponseBadRequest()


def get_year_overview(request):
    if (request.user.is_authenticated() and request.is_ajax()):
        tch_id = request.user.user_id
        year = request.GET["year"]
        table = get_average_grade_for_year(tch_id, year)
        return HttpResponse(json.dumps(table))
    return HttpResponseBadRequest()

def get_class_overview(request):
    if (request.user.is_authenticated() and request.is_ajax()):
        tch_id = request.user.user_id
        year = request.GET["year"]
        cls = request.GET["cls"]
        table = get_average_grade_for_class(tch_id, year, cls)
        return HttpResponse(json.dumps(table))
    return HttpResponseBadRequest()


def get_assignment_overview(request):
    if (request.user.is_authenticated() and request.is_ajax()):
        tch_id = request.user.user_id
        cls = request.GET["cls"]
        as_name = request.GET["as_name"]
        table = get_student_grades_for_assingments(tch_id, cls, as_namef)
        return HttpResponse(json.dumps(table))
    return HttpResponseBadRequest()
