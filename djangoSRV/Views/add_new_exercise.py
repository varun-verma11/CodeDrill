from django.http import HttpResponse, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template
from utils import get_header_navbar
from Forms import NewExerciseForm

def add_new_exercise(request):
	if (request.user.is_authenticated()):
		menu = get_template("teacher_menu.html").render(Context({ 'page':'add_ex'}))
		elements = get_header_navbar("Teacher",request.user.first_name + " " + request.user.last_name,"Add New Exercise")
		template = get_template("add_new_exercise.html")
		new_ex_form = NewExerciseForm()
		context =  Context({ 'header' : elements['header'],
                            'navbar' : elements['navbar'],
                            'menu' : menu,
                            'new_ex' : new_ex_form
                           });
		return HttpResponse(template.render(context));
	return HttpResponseBadRequest()