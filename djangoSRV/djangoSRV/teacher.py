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
    #print request.method
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

def authenticateTeacher(request):
    parameters = request.GET
    teacher = Teacher.objects.filter(uname__exact = parameters['username'], pw = parameters['password'])
    return len(teacher) == 1

def sendExercisesToClass(request):
    parameters = request.GET
    ex_id = parameters['ex_id']
    c_id = parameters['c_id']
    row = AssignedExercises(ex_id=ex_id, c_id=c_id)
    row.save()    

def viewSubmissionMark(request):
    students = Student.objects.all()
    submissions = StudentSubmission.objects.all()
    ret = []
    for student in students:
        ret_aux = []
        submission = StudentSubmission.objects.filter(stu_id__exact=student.stu_id)
        ret_aux.append(student.name)
        ret_aux.append(submission[0].result)
        #print ret_aux
        ret.append(ret_aux)
    return ret