from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.template.loader import get_template
from django.template import Context



def logout_user(request):
	if (request.user.is_authenticated()):
		logout(request)
		template = get_template("logout.html")
		return HttpResponse(template.render(Context()))
	return HttpResponseRedirect("/")