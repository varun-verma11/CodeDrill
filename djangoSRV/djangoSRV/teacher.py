from model.models import *
from Views.teaching_data_structure import TeachingHierarchy, SchoolYear, TeachingClass
from Views.exercise_data_structure import AssignmentsBook, Chapter, Assignment
from django.db.models import Avg

def get_exercise(ex_id):
    arr = Exercise.objects.filter(ex_id=ex_id).values_list()
    return arr[0]

def add_students_to_course(student_names, course_id):
    #course = Course.objects.filter(c_id=course_id).first()
    for std_name in student_names:
        student = Student.objects.filter(uname=std_name)[0]
        Course.objects.filter(c_id=course_id)[0].students.add(student)

def delete_students_from_course(student_ids, course_id):
    #course = Course.objects.filter(c_id=course_id).first()
    print "Deleting student from class"
    for stu_id in student_ids:
        student = Student.objects.filter(user_id=stu_id)[0]
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
        classes = courses.filter(year__exact=year).values('name','c_id')
        school_classes = []
        for cls in classes:
            '''

                **********************************************
                **********************************************
                **********************************************
                **********************************************
                
                DUDE WE NEED THIS FIXED!!!!
                Here for each of the classes, you could be adding
                the assignments assigned to them.

                I guess u can somehow use the one's from student.py 

                

                **********************************************
                **********************************************
                **********************************************
                **********************************************
            '''
            as1 = Assignment("Assignment 1", 1)
            as2 = Assignment("Assignment 2", 2)
            school_classes.append(TeachingClass(cls['name'],cls['c_id'], assignments=[as1, as2]))
        school_years.append(SchoolYear(str(year), school_classes))
    return TeachingHierarchy(school_years)

#a cleaner variant of the above, prone to testing
def get_courses_with_assignments2(tch_id):
    courses = Course.objects.filter(tch_id__exact=tch_id).prefetch_related('assignedexercises_set')
    asgn_years = courses.values_list('year', flat=True).distinct()
    # now for setting the hierarchy, a huge piece of magic
    h = TeachingHierarchy(  [SchoolYear(str(y), 
                                [TeachingClass(c.name, c.c_id,
                                    assignments=[Assignment(str(a), a.pk)
                    for a in c.assignedexercises_set.all()])
                for c in courses.filter(year__exact=y)]) 
            for y in asgn_years])
    #list comprehension            
    return h

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
    course = Course.objects.get(c_id=course_id)
    new_assignment = AssignedExercises(ex_id=exercise, c_id=course)
    new_assignment.save()
    return True

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

    return [a for cls in [c.c_id for c in Teacher.objects.get(user_id__exact=tch_id).course_set.filter(year__exact=year)]
                for a in get_average_grade_for_class(tch_id,year,cls)]

def delete_class(cls_id):
    print "deleting class: ", cls_id
    return 0;

def get_average_grade_for_class(tch_id, year, cls):
    ass = AssignedExercises.objects.filter(c_id__exact=cls)
    ret = []
    return  [{  'as_name': a.ex_id.title, 
                'grade': LatestStudentScore.objects.filter(ex_id=a.ex_id).aggregate(Avg('score'))['score__avg']
             }
            for a in ass]
#    for a in ass:
#        ex=a.ex_id
#        avg_score = LatestStudentScore.objects.filter(ex_id=ex.ex_id).aggregate(Avg('score'))
#        ret.append({'as_name':ex.title, 'grade':avg_score['score__avg']})
#    return ret

def get_student_grades_for_assingments(tch_id, cls_id, as_id):
    ret = []
    #for course in Course.objects.filter(tch_id=tch_id):
    c_id = cls_id
    ass_exercise = AssignedExercises.objects.get(c_id=c_id)
    ex_id = ass_exercise.ex_id_id
    exercise = Exercise.objects.get(ex_id=ex_id)
    scores = LatestStudentScore.objects.filter(ex_id=ex_id)
    for score in scores:
        student = Student.objects.get(user_id=score.stu_id.user_id)
        ret.append({'student':student.first_name + " " + student.last_name + " (" + student.uname + ")",'as_name':exercise.title, 'grade':score.score})
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

# gets one submission of the student for a given assignment
# TODO: change it to pick up the right submission
# TODO: put assignment description as well
def get_submission_by(stu_id, asgn_id):
    submissions = StudentSubmission.objects.filter(stu_id__exact=stu_id, assign_id__pk__exact=asgn_id)
    asgns = AssignedExercises.objects.filter(pk__exact=asgn_id).select_related('ex_id__description')
    # obtaining data independently
    code = submissions[0].content.encode("utf8") if submissions else None
    q = asgns[0].ex_id.description.encode("utf8") if asgns else None
    return { 'q': q,
             'code':code
           }
