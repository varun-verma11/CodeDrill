from model.models import Student

def submit_exercise(request):
    parameters = REQUEST.GET
    stu_id = parameters["stu_id"]
    ex_id  = parameters["ex_id"]
    score  = parameters["score"]
    row = LatestStudentScore(stu_id = stu_id, ex_id = ex_id, score = score)
    row.save()

def get_score(request):
    pass