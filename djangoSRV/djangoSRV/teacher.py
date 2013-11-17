from model.models import *
from Views.teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from Views.exercise_data_structure import AssignmentsBook, Chapter, Assignment

def add_students_to_course(student_ids, course_id):
    #course = Course.objects.filter(c_id=course_id).first()
    for std_id in student_ids:
        student = Student.objects.filter(user_id=std_id).first()
        Course.objects.filter(c_id=course_id).first().students.add(student)

def delete_students_to_course(student_ids, course_id):
    #course = Course.objects.filter(c_id=course_id).first()
    for std_id in student_ids:
        student = Student.objects.filter(user_id=std_id).first()
        Course.objects.filter(c_id=course_id).first().students.remove(student)
   
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
        # print sub
        # submission.submit_timemission.stu_id, submission.ex_id, submission.content, submission.submit_time
        ret2 = []
        ret2.append(submission.user_id)
        # ret2.append(submission.ex_id)
        ret2.append(submission.assign_id.ex_id)
        ret2.append(submission.content)
        ret2.append(submission.submit_time)
        ret.append(ret2)
        # needs more cowbell and HttpResponse
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

def get_all_exercises():
    categories = Exercise.objects.values_list('category').distinct()
    chapters = []

    for category in categories:
        assignments = []
        ascii_cat = category[0].encode("ascii")
        for exercise in Exercise.objects.filter(category=ascii_cat):
            assignment = Assignment(exercise.title, exercise.ex_id, exercise.content, exercise.description)
            assignments.append(assignment)      
        chapter = Chapter(ascii_cat, assignments)
        chapters.append(chapter)

    
    return AssignmentsBook(chapters)

def get_courses(tch_id):
    courses = Course.objects.filter(tch_id__exact=tch_id)
    years = []
    for course in courses:
        if course.year not in years:
            years.append(course.year)

    school_years = []
    for year in years:
        classes = courses.filter(year=year).values('name','c_id')
        school_classes = []
        for cls in classes:
            school_classes.append(TeachingClass(cls['name'],cls['c_id']))
        school_years.append(SchoolYear(str(year), school_classes))

    return TeachingHierarchy(school_years)

def get_students_in_course(course_id):
    try:
        course = Course.objects.filter(c_id=course_id)[0]
    except IndexError:
        return ([],[])
    students = []
    for student in course.students.all():
        students.append({  'full_name':student.first_name.encode("utf8") + " " + student.last_name.encode("utf8"),
                        'uname' : student.uname
                    })
    return students

def add_new_course(name,year, tch_id):
    #create course and save it
    return True

def get_suggested_names(start):
    names = []
    students = Student.objects.filter(first_name__contains=start).values("first_name", "last_name",'uname')
    for std in students:
        names.append({'name':std["first_name"] + " " + std["last_name"], "uname": std["uname"]})
    return names

def rename_course(c_id, name):
    try:
        Course.objects.filter(c_id=c_id).update(name=name)
        return True
    except IndexError:
        return False


def viewSubmissionMark(request):
    students = Student.objects.all()
    submissions = StudentSubmission.objects.all()
    ret = []
    for student in students:
        ret_aux = []
        submission = StudentSubmission.objects.filter(stu_id__exact=student.user_id)
        # ret_aux.append(student.name)
        # ret_aux.append(submission[0].result)
        # print ret_aux
        # ret.append(ret_aux)
        if submission:
            ret_aux.append(student.name)
            ret_aux.append(submission[0].result)
            ret.append(ret_aux)
            # needs more cowbell and a HttpResponse
    return ret
