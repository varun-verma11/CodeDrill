from django.db import models

# Create your models here.

class Exercises(models.Model):
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Content', blank=True)
    description = models.TextField('Description')
