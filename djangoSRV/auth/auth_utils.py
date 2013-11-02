from django.shortcuts import redirect

# determines whether the session is authenticated or not 
def is_authenticated_session(request):
    return 'user_id' in request.session


# determines whether the user has permission to access some object
# STUB
def has_permission(request):
    return True

# redirects to the login page
# STUB
def redirect_to_login(request):
    return redirect('login');


# logs a user
def login(request):
    if is_authenticated_session(request):
        return
    pass
    
   
