from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context
from auth import auth_utils

def view_spec(request):
	if (request.user.is_authenticated()):
		template = get_template("view_spec.html")
		context = Context()
		return HttpResponse(template.render(context))
	return HttpResponseRedirect("/")