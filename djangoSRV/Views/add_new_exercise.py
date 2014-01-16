from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from utils import get_header_navbar
from Forms import NewExerciseForm
from django.core.context_processors import csrf
from djangoSRV.teacher import create_new_exercise

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
		context.update(csrf(request))
		return HttpResponse(template.render(context));
	return HttpResponseBadRequest()

def create_exercise(request):
	if (request.user.is_authenticated()):
		form = NewExerciseForm(request.POST)
		if(form.is_valid()):
			title = form.cleaned_data["title"]
			chapter = form.cleaned_data["chapter"]
			description = form.cleaned_data["description"]
			code = form.cleaned_data["code"]
			sample_answer = form.cleaned_data["sample_answer"]
			create_new_exercise(title, chapter, description, code, sample_answer)
		return HttpResponseRedirect("/teacher/add-new-exercise/");
	return HttpResponseBadRequest()	