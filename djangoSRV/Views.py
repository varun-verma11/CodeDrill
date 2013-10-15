#!/usr/bin/env python

from django.http import HttpResponse

def getGrades(request):
	return HttpResponse("Content-Type: text/html" +
	 	"""\
		<html>
		<body>
		<h2>Hello World!</h2>
		</body>
		</html>
		""")
