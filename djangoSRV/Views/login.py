from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def login(request):
	context = Context();
	template = get_template("login.html");
	return HttpResponse(template.render(context))
