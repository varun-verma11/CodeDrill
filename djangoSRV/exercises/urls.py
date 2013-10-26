from django.conf.urls import patterns, url

from exercises import views

urlpatterns = patterns('', 

    url(r'/get_ex/$', views.retrieve_exercise),
)
