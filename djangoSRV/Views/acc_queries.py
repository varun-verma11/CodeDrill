from model.models import Student, Teacher

def get_table_by_type(user_type):
    if user_type == 'teacher':
        return Teacher
    if user_type == 'student':
        return Student
    return None

def update_password(old_password, new_password, uid, user_type):
    user = get_table_by_type(user_type)


    user_entry = user.objects.filter(user_id=uid).first()

    if not user_entry.pw == old_password:
        return False

    user.objects.filter(user_id=uid).update(pw=new_password)
    return True

def update_email(new_email, uid, user_type):
    user = get_table_by_type(user_type)
    user.objects.filter(user_id=uid).update(email=new_email)
