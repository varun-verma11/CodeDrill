import sys
import os
#sys.path.append('../frontend/')
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../frontend')
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Views')


from django.conf.urls import patterns, include, url
from django.contrib import admin
from Views.grades_view import get_grades_view
from teacher import *
from Views.teacher_view import get_teacher_view
from Views.set_exercise import get_set_exercise_page
from Views.authenticate import authenticate
from Views.login import login



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grades/', get_grades_view),
    url(r'^teacher/', viewSubmissionMark),
    url(r'^teacher_view/', get_teacher_view),
    url(r'^set_exercise/', get_set_exercise_page),
    url(r'^authenticate', authenticate),
    url(r'^', login)
)
