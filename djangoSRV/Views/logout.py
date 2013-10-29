from django.http import HttpResponse
from django.contrib.auth import logout


def logout_user(request):
	logout(request)
	return HttpResponse("you have succesfully logout <br> <a href='/' > Home page</a>")