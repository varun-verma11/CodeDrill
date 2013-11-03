# This file registers all the models to the general django admin site.
# It's only useful for monitoring and changing the database state in
# a graphical context

from django.contrib import admin
from model.models import *

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exercise, AuthorAdmin)
admin.site.register(ModelSolution, AuthorAdmin)
admin.site.register(StudentSubmission, AuthorAdmin)
admin.site.register(Test, AuthorAdmin)
admin.site.register(AssignedExercises, AuthorAdmin)
admin.site.register(Course, AuthorAdmin)
admin.site.register(Student, AuthorAdmin)
admin.site.register(Teacher, AuthorAdmin)
