import sys
sys.path.insert(0, '/home/varun/Work/CodeDrill/djangoSRV/frontend/')

from django.conf.urls import patterns, include, url
from django.contrib import admin
from grades_html_view import get_grades_page

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grades/$', get_grades_page)
)
