from django.db import models

# Create your models here.
# DID: explicit reference for foreign keys;
#      many-to-many relationship for course registration
# TODO: think about separating whether centralising it like this is optimal

# easier to just use this as choices for school years in course 


class Exercise(models.Model):
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Content', blank=True)
    description = models.TextField('Description')


class ModelSolution(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id', primary_key=True)
    content = models.TextField('Content')


class StudentSubmission(models.Model):
    stu_id = models.ForeignKey('Student', to_field='stu_id')
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    content = models.TextField('Content', blank=True)
    submit_time = models.DateTimeField('Time of Submission',
        auto_now_add=True)


class Test(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    test_content = models.TextField('Test Content')


class Course(models.Model):
    # easier to just use this as choices for school years in course 
    SCHOOL_YEAR_CHOICES = (
        ( 1 , '1'),
        ( 2 , '2'),
        ( 3 , '3'),
        ( 4 , '4'),
        ( 5 , '5'),
        ( 6 , '6'),
        ( 7 , '7'),
        ( 8 , '8'),
        ( 9 , '9'),
        ( 10 , '10'),
        ( 11 , '11'),
        ( 12 , '12'),
    )
    c_id = models.AutoField('Course ID', primary_key=True)
    name = models.CharField('Course Name', max_length=50)
    year = models.IntegerField('Year', choices = SCHOOL_YEAR_CHOICES)
    tch_id = models.ForeignKey('Teacher', to_field = 'tch_id')
    students = models.ManyToManyField('Student')


class Teacher(models.Model):
    tch_id = models.AutoField('Teacher ID', primary_key=True)
    name = models.CharField('Name', max_length=50)


class Student(models.Model):
    stu_id = models.AutoField('Teacher ID', primary_key=True)
    name = models.CharField('Name', max_length=50)


