from exercises.models import *
from django.http import HttpResponse

def listAllTeachers(request):
    teachers = Teacher.objects.all()
    ret = []
    for teacher in teachers:
        #print teacher.name
        ret.append(teacher.name)
    return ret

def viewSubmissions(request):
    print request.method
    submissions = StudentSubmission.objects.all()
    ret = []
    for submission in submissions:
        print sub
        submission.submit_timemission.stu_id, submission.ex_id, submission.content, submission.submit_time
        ret2 = []
        ret2.append(submission.stu_id)
        ret2.append(submission.ex_id)
        ret2.append(submission.content)
        ret2.append(submission.submit_time)
        ret.append(ret2)
    return ret

def authenticateStudent(request):
    pass

def sendExercisesToClass(request):
    pass

def viewSubmissionMark(request):
    pass
