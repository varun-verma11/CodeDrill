import sys
import os
#sys.path.append('../frontend/')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../frontend')


from django.conf.urls import patterns, include, url
from django.contrib import admin
from grades_html_view import get_grades_page
from django.contrib import admin
from teacher import listAllTeachers

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grades/', get_grades_page),
    url(r'^teacher/', listAllTeachers)
)
