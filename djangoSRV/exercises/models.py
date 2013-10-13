from django.db import models

# Create your models here.

class Exercise(models.Model):
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Content', blank=True)
    description = models.TextField('Description')


class ModelSolution(models.Model):
    ex_id = models.ForeignKey('Exercise', primary_key=True)
    content = models.TextField('Content')

class StudentSubmission(models.Model):
    stu_id = models.ForeignKey('Student')
    ex_id = models.ForeignKey('Exercise')
    content = models.TextField('Content', blank=True)
    submit_time = models.DateTimeField('Time of Submission',
        auto_now_add=True)


class Teacher(models.Model):
    tch_id = models.AutoField('Teacher ID', primary_key=True)
    name = models.CharField('Name', max_length=50)


class Student(models.Model):
    stu_id = models.AutoField('Teacher ID', primary_key=True)
    name = models.CharField('Name', max_length=50)


