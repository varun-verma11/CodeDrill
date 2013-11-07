#file for registering the model to the admin site
from django.contrib import admin
from u_model.models import *

admin.site.register(Exercise)
admin.site.register(ModelSolution)
admin.site.register(StudentSubmission)
admin.site.register(Test)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
