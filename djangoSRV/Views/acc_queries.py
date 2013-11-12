from model.models import Student, Teacher

def update_password(old_password, new_password, uid, user_type):
    user = None
    if user_type == 'teacher':
        user = Teacher
        id_field_name='tch_id'

    if user_type == 'student':
        user = Student
        id_field_name='stu_id'

    #This won't work for student: TODO need to fix
    user_arr = user.objects.filter(tch_id=uid)
    user_entry = user_arr.first()
    if not user_entry.pw == old_password:
        return False

    user.objects.filter(tch_id=uid).update(pw=new_password)
    return True

