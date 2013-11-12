# The registration handlers for both student and teacher.
# As of this version, usernames are unique, in order to
# enforce disjunction between the Teacher and Student
# tables.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import resolve, reverse
from u_model.views.utils.Forms import StudentRegisterForm, TeacherRegisterForm
from u_model.models import Student, Teacher





# Checks whether a user with given username already exists
def user_exists(uname):
    return User.objects.filter(username=uname).exists()



# Registers the student with a username and adds an entry
# in the Students table. Courtesy of ... Mihai Jiplea? Varun Verma?
def register_student(request):
    form = StudentRegisterForm(request.POST)
    if (not form.is_valid()):
        return HttpResponse('The data you provided was incomplete. Try again.')
    # We have valid data, checking for duplicate
    cd = form.cleaned_data
    if(user_exists(cd['reg_username'])):
        return HttpResponse('Username already exists :(. Try another one')
    # We can make the User and all else that is needed
    user = User.objects.create_user(
               username   = cd['reg_username'],
               password   = cd['reg_password'],
               first_name = cd['first_name'],
               last_name  = cd['last_name'],
               email      = cd['email'] )
    stu_entry = Student(stu_id=user)
    stu_groups = Group.objects.filter(name = 'Students')
    # Now save the info
    stu_entry.save()
    if(stu_groups.exists()):
        user.groups.add(stu_groups[0])
        user.save()
    # Send a redirect to the student-login
    view = resolve(request.path)
    login_redirect_url = reverse(view.namespace + ':' + 'student-login')
    return HttpResponseRedirect(login_redirect_url)



# The same as register_student, but for teachers.
def register_teacher(request):
    form = TeacherRegisterForm(request.POST)
    if (not form.is_valid()):
        return HttpResponse('The data you provided was incomplete. Try again.')
    # We have valid data, checking for duplicate
    cd = form.cleaned_data
    if(user_exists(cd['reg_username'])):
        return HttpResponse('Username already exists :(. Try another one.')
    # We can make the User and all else that is needed
    user = User.objects.create_user(
               username   = cd['reg_username'],
               password   = cd['reg_password'],
               first_name = cd['first_name'],
               last_name  = cd['last_name'],
               email      = cd['email'] )
    tch_entry = Teacher(tch_id=user)
    tch_groups = Group.objects.filter(name = 'Students')
    # Now save the info
    tch_entry.save()
    if(tch_groups.exists()):
        user.groups.add(tch_groups[0])
        user.save()
    # Send a redirect to the student_login
    view = resolve(request.path)
    login_redirect_url = reverse(view.namespace + ':' + 'teacher-login')
    return HttpResponseRedirect(login_redirect_url)

