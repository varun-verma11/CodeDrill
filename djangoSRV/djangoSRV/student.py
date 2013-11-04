from model.models import Student, LatestStudentScore

def submit_exercise(request):
    parameters = request.GET
    stu_id = parameters["stu_id"]
    ex_id  = parameters["ex_id"]
    score  = parameters["score"]
    row = LatestStudentScore(stu_id = stu_id, ex_id = ex_id, score = score)
    row.save()

def get_score(request):
    parameters = request.GET
    ex_id = parameters["ex_id"]
    stu_id = parameters["stu_id"]
	arr = LatestStudentScore.objects.filter(ex_id=ex_id, stu_id=stu_id)
	return arr[0]