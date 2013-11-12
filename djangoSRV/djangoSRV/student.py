from model.models import Student, LatestStudentScore, Exercise, AssignedExercises, Student, Course, Exercise
from Views.exercise_data_structure import AssignmentsBook, Chapter, Assignment


def submit_exercise(ex_id, stu_id, score):
    row = LatestStudentScore(stu_id = stu_id, ex_id = ex_id, score = score)
    row.save()

def get_score(ex_id, stu_id):
	arr = LatestStudentScore.objects.filter(ex_id=ex_id, stu_id=stu_id).values()
	return arr[0]['score']

def get_exercise(ex_id):
	arr = Exercise.objects.filter(ex_id=ex_id).values_list()
	return arr[0]

def get_number_of_submissions(stu_id):
    return 0

def get_grades(stu_id, page_num):
    return ["1","Chapter", "Problem Name", "Grade/Mark"]

def getStudentAssignments(uid):
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
        ascii_cat = category[0].encode("ascii")
        for exercise in Exercise.objects.filter(category=ascii_cat):
            assignment = Assignment(exercise.title, exercise.ex_id, exercise.content)
            assignments.append(assignment)   	
        chapter = Chapter(ascii_cat, assignments)
        chapters.append(chapter)
    return AssignmentsBook(chapters)

