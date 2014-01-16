from model.models import Student, LatestStudentScore, Exercise, AssignedExercises, Student, Course, Exercise, StudentSubmission, Feedback, Teacher
from Views.exercise_data_structure import AssignmentsBook, Chapter, Assignment

def get_course_ids_by_std_id(user_id):
    course_ids = []

    for course in Course.objects.all():
        student_entries = course.students.filter(user_id=user_id)
        if(student_entries.count() > 0):
            course_ids.append(course.c_id)
    return course_ids

def submit_exercise_code(stu_id, ex_id, code):
    assign = AssignedExercises.objects.filter(ex_id=ex_id)[0]
    submission = StudentSubmission(stu_id=stu_id, assign_id=assign, content=code)
    submission.save()

def submit_exercise_score(ex_id, user_id, score):
    arr = LatestStudentScore.objects.filter(ex_id=ex_id, stu_id=user_id)
    if len(arr) >= 1:
        p = LatestStudentScore.objects.get(ex_id=ex_id, stu_id=user_id)
        p.score = score
        p.save()
    else:
        row = LatestStudentScore(stu_id = user_id, ex_id = ex_id, score = score)
        row.save()

def get_score(ex_id, user_id):
    arr = LatestStudentScore.objects.filter(ex_id=ex_id, stu_id=user_id).values()
    return arr[0]['score']

def get_exercise(ex_id):
    arr = Exercise.objects.filter(ex_id=ex_id).values_list()
    return arr[0]

def submit_feedback_for_student(stu_id, tch_id, ex_id, feedback):
    #print stu_id,  tch_id, ex_id, feedback
    assign_id = ex_id
    sub_id = StudentSubmission.objects.order_by('-pk').filter(stu_id=stu_id, assign_id=assign_id)[0]
    teacher = Teacher.objects.get(user_id=tch_id)
    row = Feedback(tch_id=teacher, sub_id=sub_id, content=feedback)
    row.save()
    return True

def get_number_of_submissions(user_id):
    return LatestStudentScore.objects.filter(stu_id=user_id).count()

def get_feedback_for_student(ex_id, stu_id):
    code = "No code submitted"
    feedback = "No feedback submitted by teacher"
    assigned = AssignedExercises.objects.get(ex_id=ex_id)
    arr = StudentSubmission.objects.order_by('-pk').filter(stu_id=stu_id, assign_id=assigned)

    if len(arr) >= 1:
        code = arr[0].content
        c_id = AssignedExercises.objects.get(ex_id=ex_id).c_id.c_id
        tch_id = Course.objects.get(c_id=c_id).tch_id
        arr2 = Feedback.objects.order_by('-pk').filter(sub_id=arr[0], tch_id=tch_id)
        if len(arr2) >=1:
            feedback = arr2[0].content

    return {'code': code, 'feedback':feedback}

def get_grades(user_id, page_num, page_size):
    course_ids = get_course_ids_by_std_id(user_id)
    ex_ids = []

    for exco in AssignedExercises.objects.all():
        if exco.c_id_id in course_ids:
            ex_ids.append(exco.ex_id_id)
    ret = []
    iterator = 0
    for ex_id in ex_ids:
        aux_row = []
        iterator += 1
        ex_row = Exercise.objects.filter(ex_id=ex_id)[0]
        aux_row.append(iterator)
        aux_row.append(ex_row.category)
        aux_row.append(ex_row.title)
        submission_row = LatestStudentScore.objects.filter(stu_id=user_id, ex_id=ex_id)
        if len(submission_row) == 0:
            aux_row.append("N/A")
        else:
            score = submission_row[0].score
            aux_row.append(score)
        ret.append(aux_row)

    return ret

def getStudentAssignments(uid):
    one_st_array = Student.objects.filter(user_id=uid)
    user_id = one_st_array[0].user_id
    course_ids = get_course_ids_by_std_id(user_id)
    ex_ids = []

    #Get the exercises assigned to the courses that the
    #student is subscribed to
    print course_ids
    for exco in AssignedExercises.objects.all():
        if exco.c_id_id in course_ids:
            ex_ids.append(exco.ex_id_id)

    chapters = []
    print ex_ids
    categories = Exercise.objects.values_list('category').distinct()
    for category in categories:
        assignments = []
        ascii_cat = category[0].encode("ascii")
        for exercise in Exercise.objects.filter(category=ascii_cat):
            if exercise.ex_id in ex_ids:
                assignment = Assignment(exercise.title, exercise.ex_id, exercise.content, exercise.description)
                assignments.append(assignment)
        if len(assignments) > 0:
            chapter = Chapter(ascii_cat, assignments)
            chapters.append(chapter)
    return AssignmentsBook(chapters)

