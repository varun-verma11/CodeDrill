from django.http import HttpResponse
from teacher_view import get_teacher_view_with_username

def __check_if_valid_login(username, password):
	return True

def __is_user_teacher(username):
	return True

def authenticate(request):
	args = request._get_get()
	username = args.get("username")
	password = args.get("password")
	# if (__check_if_valid_login(username, password)):
	# 	if (__is_user_teacher(username)):
	# 		return get_teacher_view_with_username(username)
	# 	else if (__is_user_student(username)):
	# 		return 

	return HttpResponse(" Hello username:" + username + " password:" + password)