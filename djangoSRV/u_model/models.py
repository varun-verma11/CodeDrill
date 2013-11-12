from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# DID: explicit reference for foreign keys;
#      many-to-many relationship for course registration
# TODO: think whether centralising it like this is optimal
#       password hiding



############################################################
#### USER TABLES ###########################################


class Teacher(models.Model):
    # tch_id = models.AutoField(primary_key=True)
    # uname = models.CharField('Teacher ID', max_length=15, unique=True)
    # name = models.CharField('Name', max_length=50)
    # first_name = models.CharField('First Name', max_length=50)
    # last_name = models.CharField('Last Name', max_length=50)
    # email = models.CharField('Email', max_length=50)
    # pw = models.CharField('Password', max_length=50)
    # last_login = models.DateTimeField(auto_now=True)
    tch_id = models.ForeignKey(User, primary_key=True,
                               on_delete=models.CASCADE)

    def __unicode__(self):
        return self.tch_id.username
    # def is_authenticated(user_id):
        # return True   
    #def is_type(self, asserted_type):
        # print "Checkpoint 4"
        # return asserted_type == "Teacher"
    # def is_active(self):
        # return False
    # def is_staff(self):
        # return False


class Student(models.Model):
    # stu_id = models.AutoField(primary_key=True)
    # uname = models.CharField('Student ID', max_length=15, unique=True)
    # first_name = models.CharField('First Name', max_length=50)
    # last_name = models.CharField('Last Name', max_length=50)
    # email = models.CharField('Email', max_length=50)
    # pw = models.CharField('Password', max_length=50)
    # last_login = models.DateTimeField(auto_now=True)
    # Course has a Many to Many relationship with this, so you can find things
    stu_id = models.ForeignKey(User, primary_key=True,
                               on_delete=models.CASCADE)

    def __unicode__(self):
        return self.stu_id.username
    # def is_authenticated(user_id):
        # return True
    # def is_type(self, asserted_type):
        # print "Checkpoint 5"
        # return asserted_type == "Student"
    # '''def is_active(self):
        # return False
    # def is_staff(self):
        # return False
    # def has_module_perms(self, nomatter):
        # return False'''


############################################################
#### COURSES ###############################################


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
    teachers = models.ManyToManyField(Teacher)
    students = models.ManyToManyField(Student)

    def __unicode__(self):
        return self.name + ' - Year ' + str(self.year)


############################################################
#### EVERRYTHING ELSE ######################################

class Exercise(models.Model):
    ex_id = models.AutoField('Exercise ID', primary_key=True)
    title = models.CharField('Title', max_length=100)
    category = models.CharField('Category', max_length=100)
    content = models.TextField('Content', blank=True)
    description = models.TextField('Description')

    def __unicode__(self):
        return self.category + ' - ' + self.title


class ModelSolution(models.Model):
    ex_id = models.ForeignKey(Exercise, primary_key=True)
    content = models.TextField('Content')
    
    def __unicode__(self):
        return 'Solution for ' + self.ex_id.__unicode__()


class Assignment(models.Model):
    ex_id = models.ForeignKey(Exercise)
    c_id = models.ForeignKey(Course)


class StudentSubmission(models.Model):
    stu_id = models.ForeignKey(Student)
    assign_id = models.ForeignKey(Assignment)
    content = models.TextField('Content', blank=True)
    submit_time = models.DateTimeField('Time of Submission',
        auto_now_add=True)
    result = models.DecimalField(max_digits=3, decimal_places=2)

               
class Test(models.Model):
    ex_id = models.ForeignKey(Exercise)
    test_content = models.TextField('Test Content')



    def __unicode__(self):
        return self.c_id.__unicode__() + ' --- ' + self.ex_id.__unicode__()


# class LatestStudentScore(models.Model):
    # stu_id = models.ForeignKey('Student', to_field='stu_id')
    # ex_id  = models.ForeignKey('Exercise', to_field='ex_id')
    # score = models.TextField('Score', default='N/A')

