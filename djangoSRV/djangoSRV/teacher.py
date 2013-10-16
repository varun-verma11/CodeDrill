from exercises.models import Teacher

def listAllTeachers(request):
    teacher1 = Teacher.objects.all()
    ret = []
    for teacher in teachers:
        print teacher.name
        ret.append(teacher.name)
    return ret

def viewSubmissions(request):
    pass

def sendExercisesToClass(request):
    pass

def viewSubmissionMark(reques):
    pass
