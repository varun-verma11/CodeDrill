# This file registers all the models to the general django admin site.
# It's only useful for monitoring and changing the database state in
# a graphical context

from django.contrib import admin
from djangoSRV.models import *

admin.site.register(Exercise)
admin.site.register(ModelSolution)
admin.site.register(StudentSubmission)
admin.site.register(Test)
admin.site.register(AssignedExercises)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
