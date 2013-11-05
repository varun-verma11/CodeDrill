from model.models import Student, LatestStudentScore

def submit_exercise(ex_id, stu_id, score):
    row = LatestStudentScore(stu_id = stu_id, ex_id = ex_id, score = score)
    row.save()

def get_score(ex_id, stu_id):
	arr = LatestStudentScore.objects.filter(ex_id=ex_id, stu_id=stu_id).values()
	return arr[0]['score']

def get_exercise(ex_id):
	arr = Exercise.objects.filter(ex_id=ex_id).values_list()
	return arr[0]
