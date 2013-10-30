from django.conf.urls import patterns, include, url
from django.contrib import admin
from Views.grades_view import get_grades_view
from teacher import *
from Views.teacher_view import get_teacher_view
from Views.set_exercise import get_set_exercise_page
from Views.authenticate import authenticate_student, authenticate_teacher
from Views.login import student_login, teacher_login
from Views.register import register_student, register_teacher
from Views.student_view import get_student_view
from Views.submit_code import submit_student_code
from Views.single_exercise_code_view import single_exercise_view
from Views.student_grades import student_grades_view
from Views.home import home_page
from Views.logout import logout_user
from Views.view_spec import view_spec

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grades/$', get_grades_view),
    url(r'^teacher/$', viewSubmissionMark),
    url(r'^teacher-view/$', get_teacher_view),
    url(r'^set-exercise/$', get_set_exercise_page),
    url(r'^authenticate_student/$', authenticate_student),
    url(r'^authenticate_teacher/$', authenticate_teacher),
    url(r'^student-login/$', student_login),
    url(r'^teacher-login/$', teacher_login),
    url(r'^register-student/$', register_student),
    url(r'^register-teacher/$', register_teacher),
    url(r'^student-view/$', get_student_view),
    url(r'^submit-code/(\d+)/$', submit_student_code),
    url(r'^code-single-exercise/(\d+)/$', single_exercise_view),
    url(r'^student-grades/$', student_grades_view),
    url(r'^logout/$', logout_user),
    url(r'^view-spec/$', view_spec),
    url(r'^$', home_page)
)
