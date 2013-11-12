from django.conf.urls import patterns, url, include
from u_model.views.auth.register import register_student, register_teacher
from u_model.views.auth.login import student_login, teacher_login
from u_model.views.home import home_page

urlpatterns = patterns('',
    url(r'^register-student/$', register_student, name='register-student'),
    url(r'^register-teacher/$', register_teacher, name='register-teacher'),
    url(r'^student-login/$', student_login, name='student-login'),
    url(r'^teacher-login/$', teacher_login, name='teacher-login'),
    url(r'^$', home_page, name = 'home-page'),
)
