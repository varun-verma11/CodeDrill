#!/usr/bin/env python

from django.http import HttpResponse
import haml
import mako.template
import os, sys
def getGrades(request):
	haml_source_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "helloWorld.haml"), "r")
	haml_source = ""
	while 1 :
		line = haml_source_file.readline();
		if not line: break
		haml_source += line

	haml_source = haml_source.decode('utf8')

	haml_nodes = haml.parse_string(haml_source)
	mako_source = haml.generate_mako(haml_nodes)
	return HttpResponse( mako.template.Template(mako_source).render_unicode())