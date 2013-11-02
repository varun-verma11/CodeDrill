from django.conf import settings
from djangoSRV.models import Student

class StudentBackend(object):
    
    def authenticate(self, username=None, password=None):
        try:
            user = Student.objects.get(uname=username, pw=password)
            return user
        except ObjectDoesNotExist:
            return None
    