from model.models import *
from Views.teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from Views.exercise_data_structure import AssignmentsBook, Chapter, Assignment
from django.db.models import Avg

def add_students_to_course(student_ids, course_id):
    #course = Course.objects.filter(c_id=course_id).first()
    for std_id in student_ids:
        student = Student.objects.filter(user_id=std_id)[0]
        Course.objects.filter(c_id=course_id)[0].students.add(student)

def delete_students_from_course(student_ids, course_id):
    #course = Course.objects.filter(c_id=course_id).first()
    for std_id in student_ids:
        student = Student.objects.filter(user_id=std_id)[0]
        Course.objects.filter(c_id=course_id)[0].students.remove(student)
   
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

def get_courses_with_assignments(tch_id):
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
            school_classes.append(TeachingClass(cls['name'],cls['c_id'], assignments=["As1","As2"]))
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
                        'user_id' : student.user_id
                    })
    return students

def add_new_course(name,year, tch_id):
    teacher = Teacher.objects.get(user_id=tch_id)
    Course(name=name, year=year, tch_id=teacher).save()


def set_assignment_for_course(ex_id, course_id):
    exercise = Exercise.objects.get(ex_id=ex_id)
    course = Course.objects.get(c_id=c_id)
    new_assignment = AssignedExercises(ex_id=exercise, c_id=course)
    new_assignment.save()

def get_average_for_all_assignments(tch_id):
    #Postponed
    ret = []
    for course in Course.objects.filter(tch_id=tch_id):
        c_id = course.c_id
        for ass_exercise in AssignedExercises.objects.filter(c_id=c_id):
            ex_id = ass_exercise.ex_id.ex_id
            exercise = Exercise.objects.get(ex_id=ex_id)
            avg_score = LatestStudentScore.objects.filter(ex_id=ex_id).aggregate(Avg('score'))
            ret.append({'as_name':exercise.title, 'grade':avg_score['score__avg']})
    return ret

'''
def get_average_for_all_assignments(tch_id):
    return [{"as_name":"Assignment 1", "grade":"10"}, {"as_name":"Assignment 2","grade":"20"}]
'''
def get_average_grade_for_year(tch_id, year):

    return [{"as_name":"Assignment 3", "grade":"30"}, {"as_name":"Assignment 4","grade":"40"}]

def get_average_grade_for_class(tch_id, year, cls):
    return [{"as_name":"Assignment 5", "grade":"50"}, {"as_name":"Assignment 6","grade":"60"}]

def get_student_grades_for_assingments(tch_id):
    ret = []
    for course in Course.objects.filter(tch_id=tch_id):
        c_id = course.c_id
        for ass_exercise in AssignedExercises.objects.filter(c_id=c_id):
            ex_id = ass_exercise.ex_id_id
            exercise = Exercise.objects.get(ex_id=ex_id)
            scores = LatestStudentScore.objects.filter(ex_id=ex_id)
            for score in scores:
                student = Student.objects.get(user_id=score.stu_id.user_id)
                ret.append({'student':student.uname,'as_name':exercise.title, 'grade':score.score})
    return ret

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
