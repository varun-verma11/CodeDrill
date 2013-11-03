from model.models import Student
from django.core.exceptions import ObjectDoesNotExist

class StudentBackend(object):
    
    def authenticate(self, username=None, password=None):
        user = None
        try:
            user = Student.objects.get(uname=username, pw=password)
        except ObjectDoesNotExist:
            pass
        return user

    def get_user(self, user_id):
        try:
            #print "Here am I!"
            return Student.objects.get(stu_id=user_id)
        except ObjectDoesNotExist:
            return None 