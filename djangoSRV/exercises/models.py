from django.db import models

# Create your models here.
# DID: explicit reference for foreign keys;
#      many-to-many relationship for course registration
# TODO: think whether centralising it like this is optimal
#       password hiding


class Exercise(models.Model):
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100)
    category = models.CharField('Category', max_length=100)
    content = models.TextField('Content', blank=True)
    description = models.TextField('Description')


class ModelSolution(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id', primary_key=True)
    content = models.TextField('Content')


class StudentSubmission(models.Model):
    stu_id = models.ForeignKey('Student', to_field='stu_id')
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    course = models.ForeignKey('Course', to_field='c_id')
    content = models.TextField('Content', blank=True)
    submit_time = models.DateTimeField('Time of Submission',
        auto_now_add=True)
    result = models.DecimalField(max_digits=3, decimal_places=2)


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

    def __unicode__(self):
        return self.name + ' - Year ' + str(self.year)

class Teacher(models.Model):
    tch_id = models.CharField('Teacher ID', max_length=15, primary_key=True)
    name = models.CharField('Name', max_length=50)
    pw = models.CharField('Password', max_length=50)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    stu_id = models.CharField('Student ID', max_length=15, primary_key=True)
    name = models.CharField('Name', max_length=50)
    # Course has a Many to Many relationship with this, so you can find things
    pw = models.CharField('Password', max_length=50)

    def __unicode__(self):
        return self.name
    

