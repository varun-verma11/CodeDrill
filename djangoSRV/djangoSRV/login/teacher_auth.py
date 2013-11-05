from model.models import Teacher
from django.core.exceptions import ObjectDoesNotExist

class TeacherBackend(object):
    
    def authenticate(self, username=None, password=None):
        user = None
        try:
            user = Teacher.objects.get(uname=username, pw=password)
        except ObjectDoesNotExist:
            pass
        return user

    def get_user(self, user_id):
        try:
            return Teacher.objects.get(tch_id=user_id)
        except ObjectDoesNotExist:
            return None 