from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context

def home_page(request):
	if(request.user is not None):
	    if (request.user.is_authenticated()):
	    	if (request.user.is_type("Teacher")):
	    		return HttpResponseRedirect("/teacher-view/")
	    	if (request.user.is_type("Student")):
	    		return HttpResponseRedirect("/student-view/")

	template = get_template("home.html")
	header = get_template("header.html").render(Context( {'loggedIn':False, 'title': "Home"}))
	return HttpResponse(template.render(Context({
				'header':header,
				'navbar': get_template("navbar.html").render(Context({'loggedIn':False}))
			})))