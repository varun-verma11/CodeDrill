from django.conf.urls import patterns, include, url
from django.contrib import admin
from teacher import *
from Views.teacher_view import get_teacher_view, get_overview, get_year_overview, get_class_overview, get_assignment_overview
from Views.set_exercise import get_set_exercise_page, send_exercise_to_class
from Views.authenticate import authenticate_student, authenticate_teacher, check_user_name_exists
from Views.login import student_login, teacher_login
from Views.register import register_student, register_teacher
from Views.student_view import get_student_view
from Views.submit_code import submit_student_code
from Views.single_exercise_code_view import single_exercise_view
from Views.student_grades import student_grades_view
from Views.home import home_page
from Views.logout import logout_user
from Views.view_spec import view_spec, get_exercise_details
from Views.settings import teacher_account_settings, student_account_settings, class_settings, change_password, change_email, get_registered_students_in_course, add_new_class, update_class_name,  update_course_students

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/$', viewSubmissionMark),
    url(r'^selectable/', include('selectable.urls')),
    url(r'^teacher/class-settings/manage-class/$', update_course_students),
    url(r'^teacher/get-overview/', get_overview),
    url(r'^teacher/get-year-overview/', get_year_overview),
    url(r'^teacher/get-class-overview/', get_class_overview),
    url(r'^teacher/get-assignment-overview/', get_assignment_overview),
    url(r'^student/changepassword/$', change_password),
    url(r'^teacher/changepassword/$', change_password),
    url(r'^teacher/get-students-in-class/$', get_registered_students_in_course),
    url(r'^teacher/add-new-class/$', add_new_class),
    url(r'^teacher/get-exercise/$', get_exercise_details),
    url(r'^teacher/update-class-name/', update_class_name),
    url(r'^teacher/submit-exercise/', send_exercise_to_class),
    url(r'^student/changeemail/$', change_email),
    url(r'^teacher/changeemail/$', change_email),
    url(r'^teacher/account-settings/', teacher_account_settings),
    url(r'^student/account-settings/', student_account_settings),
    url(r'^class-settings/', class_settings),
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
    url(r'^check-username/$', check_user_name_exists),
    url(r'^$', home_page)
)
