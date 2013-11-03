from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from Forms import SubmitCodeForm
from django.template import Context
from django.core.context_processors import csrf
from exercise_data_structure import AssignmentsBook, Chapter, Assignment
from model.models import AssignedExercises, Student, Course, Exercise

def get_student_view(request):
    #print "Checkpoint 2"
    if (request.user.is_type("Student")):
        #print "Checkpoint 3"
        assignments = __get_assignments_book()
        context = Context( {'name': request.user.first_name + " " + request.user.last_name,
                            'assignments' : assignments
                        })
        context.update(csrf(request))
        template = get_template("student_home.html")
        return HttpResponse(template.render(context))
    return HttpResponseRedirect("/")

def __get_assignments_book():
    #make sure the final involves adding the id.
    as1 = Assignment("If", 111, SubmitCodeForm(initial={'code':"if (1==1): \n\t print 2 \n"}, auto_id="id_%s_"+"111"))
    as2 = Assignment("If-then-else", 112, SubmitCodeForm(initial={'code': "if something do something else something"}, auto_id="id_%s_"+"112"))
    ch1 = Chapter("Conditionals", [as1, as2])

    as3 = Assignment("Addition", 113, SubmitCodeForm(initial={'code': "a=3; print a+3"}, auto_id="id_%s_"+"113"))
    as4 = Assignment("Subtraction", 114, SubmitCodeForm(initial={'code': "a=3; print a-3"}, auto_id="id_%s_"+"114"))
    ch2 = Chapter("Assignment", [as3, as4])

    as5 = Assignment("Print-10-Numbers", 115, SubmitCodeForm(initial={'code': "for i in range(10):\n\t print i"}, auto_id="id_%s_"+"115"))
    as6 = Assignment("Sum", 116, SubmitCodeForm(initial={'code': "sum=0\nfor i in range(10):\n\t sum+=i\n print sum"}, auto_id="id_%s_"+"116"))
    ch3 = Chapter("Loops", [as5, as6])

    return AssignmentsBook([ch1, ch2, ch3])


def getStudentAssignments(request):
    uid = request.user.id
    #name = "Student5"
    one_st_array = Student.objects.filter(stu_id=uid)
    stu_id = one_st_array[0].stu_id
    course_ids = []
    ex_ids = []
    for course in Course.objects.all():
        student_entries = course.students.filter(stu_id=stu_id)
        if(student_entries.count() > 0):
            course_ids.append(course.c_id)

    for exco in AssignedExercises.objects.all():
        if exco.c_id in course_ids:
            ex_ids.append(exco.ex_id)

    chapters = []
    categories = Exercise.objects.values_list('category').distinct()
    for category in categories:
        assignments = []
        for exercise in Exercise.objects.filter(category=category):
            assignment = Assignment(exercise.title, exercise.ex_id, exercise.content)
            assignments.append(assignment)   	
        chapter = Chapter(category, assignments)
        chapters.append(chapter)
    return AssignmentsBook(chapters)
