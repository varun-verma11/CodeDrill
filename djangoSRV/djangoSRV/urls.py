from django.conf.urls import patterns, include, url

import sys
sys.path.insert(0, '/Users/varunverma/Documents/Work/CodeDrill/djangoSRV')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from grades_test import getGrades

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoSRV.views.home', name='home'),
    # url(r'^djangoSRV/', include('djangoSRV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grades/$', getGrades)
)
