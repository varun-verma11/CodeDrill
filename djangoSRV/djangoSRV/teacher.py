from exercises.models import *
from django.http import HttpResponse

def listAllTeachers(request):
    teachers = Teacher.objects.all()
    ret = []
    for teacher in teachers:
        print teacher.name
        ret.append(teacher.name)
    return ret

def viewSubmissions(request):
    submissions = StudentSubmission.objects.all()
    ret = []
    for submission in submissions:
        print submission.stu_id, submission.ex_id, submission.content, submission.submit_time

def sendExercisesToClass(request):
    pass

def viewSubmissionMark(request):
    pass
