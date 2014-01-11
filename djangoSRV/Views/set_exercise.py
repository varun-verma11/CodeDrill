from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Context, Template
from django.core.context_processors import csrf
from utils import get_header_navbar
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from djangoSRV.teacher import get_courses, get_all_exercises, set_assignment_for_course, get_exercise
from Forms import ViewSpecificationForm

def get_set_exercise_page(request):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		template = get_template("set_exercise.html")
		teaching_hierarchy = get_courses(request.user.user_id)
		vsp_context = Context({'form':ViewSpecificationForm()})
		vsp_context.update(csrf(request))
		view_spec_form = get_template("view_spec_form.html").render(vsp_context)
		name = request.user.first_name + " " + request.user.last_name
		elements = get_header_navbar("Teacher",name,"Teaching Overview")
		context = Context( {'header' : elements['header'], 
							'menu' : get_template("teacher_menu.html").render(Context({"page":"set_ex"})),
							'teaching_hierarchy' : teaching_hierarchy,
							'navbar' : elements['navbar'],
							'assignment_book' : get_all_exercises(),
							'vsp_media' : Template("{{form.media}}").render(vsp_context), 
							'view_spec_form' : view_spec_form})
		return HttpResponse(template.render(context))
	return HttpResponseRedirect("/")

def get_view_spec_form(request, ex_id):
	if (request.user.is_authenticated() and request.user.is_type("Teacher")):
		exercise = get_exercise(ex_id);
		vsp_context = Context({'form':ViewSpecificationForm(initial={'code':exercise[3], 'description':exercise[4]})})
		vsp_context.update(csrf(request))
		view_spec_form = get_template("view_spec_form.html").render(vsp_context)
		return HttpResponse(view_spec_form)
	return HttpResponseRedirect("/")


def send_exercise_to_class(request):
	if (request.user.is_authenticated() and request.is_ajax()):
		ex_id = request.POST["exercise"]
		course_id = request.POST["group"]
		if (set_assignment_for_course(ex_id,course_id)):
			return HttpResponse("")
	return HttpResponseBadRequest()
