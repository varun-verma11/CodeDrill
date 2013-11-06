from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context

def home_page(request):
	template = get_template("home.html")
	header = get_template("header.html").render(Context( {'loggedIn':False, 'title': "Home"}))
	return HttpResponse(template.render(Context({'header':header})))