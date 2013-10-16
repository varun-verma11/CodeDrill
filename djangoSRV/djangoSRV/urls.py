from django.conf.urls import patterns, include, url

import sys
import os

sys.path.insert(0, '../frontend/')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/frontend')
from django.contrib import admin
from grades import getGrades

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
