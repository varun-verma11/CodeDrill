from selectable.base import ModelLookup
from selectable.registry import registry
from models import Student

class UserLookup(ModelLookup):
    model = Student
    search_fields = ('first_name__icontains',)

registry.register(UserLookup)