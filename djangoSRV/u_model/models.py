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

    def __unicode__(self):
        return self.category + ' - ' + self.title


class ModelSolution(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id', primary_key=True)
    content = models.TextField('Content')
    
    def __unicode__(self):
        return 'Solution for ' + self.ex_id.__unicode__()


class StudentSubmission(models.Model):
    stu_id = models.ForeignKey('Student', to_field='stu_id')
    # ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    # course = models.ForeignKey('Course', to_field='c_id')
    assign_id = models.ForeignKey('AssignedExercises')
    content = models.TextField('Content', blank=True)
    submit_time = models.DateTimeField('Time of Submission',
        auto_now_add=True)
    result = models.DecimalField(max_digits=3, decimal_places=2)

               

class Test(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    test_content = models.TextField('Test Content')


class AssignedExercises(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    c_id = models.ForeignKey('Course', to_field='c_id')

    def __unicode__(self):
        return self.c_id.__unicode__() + ' --- ' + self.ex_id.__unicode__()


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
    tch_id = models.AutoField(primary_key=True)
    uname = models.CharField('Teacher ID', max_length=15, unique=True)
    #name = models.CharField('Name', max_length=50)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    pw = models.CharField('Password', max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.uname

    def is_authenticated(user_id):
        return True
    
    def is_type(self, asserted_type):
        #print "Checkpoint 4"
        return asserted_type == "Teacher"
    def is_active(self):
        return False
    def is_staff(self):
        return False

class LatestStudentScore(models.Model):
    stu_id = models.ForeignKey('Student', to_field='stu_id')
    ex_id  = models.ForeignKey('Exercise', to_field='ex_id')
    score = models.TextField('Score', default='N/A')

class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    uname = models.CharField('Student ID', max_length=15, unique=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    # Course has a Many to Many relationship with this, so you can find things
    pw = models.CharField('Password', max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.uname
    def is_authenticated(user_id):
        return True
    
    def is_type(self, asserted_type):
        #print "Checkpoint 5"
        return asserted_type == "Student"
    
    '''def is_active(self):
        return False

    def is_staff(self):
        return False
    def has_module_perms(self, nomatter):
        return False'''
        
