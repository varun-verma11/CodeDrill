#The home page of CodeDrill
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context

def home_page(request):
	template = get_template("u_model/home.html")
	return HttpResponse(template.render(Context()))
