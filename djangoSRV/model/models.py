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
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.__str__()
    def __unicode__(self):
       return self.__str__()


class ModelSolution(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id', primary_key=True)
    content = models.TextField('Content')
    def __str__(self):
        return self.ex_id
    def __repr__(self):
        return self.__str__()
    
    def __unicode__(self):
        return 'Solution for ' + self.ex_id.__unicode__()

class Feedback(models.Model):
    #ex_id = models.ForeignKey('Exercise', to_field='ex_id', primary_key=True)
    #stu_id = models.ForeignKey('Student', to_field='user_id')
    tch_id = models.ForeignKey('Teacher', to_field = 'user_id')
    sub_id = models.ForeignKey('StudentSubmission')
    content = models.TextField('Content')
    def __str__(self):
        return 'Feedback for ' + self.sub_id.__str__()
    def __repr__(self):
        return self.__str__()

class StudentSubmission(models.Model):
    stu_id = models.ForeignKey('Student', to_field='user_id')
    # ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    # course = models.ForeignKey('Course', to_field='c_id')
    assign_id = models.ForeignKey('AssignedExercises')
    content = models.TextField('Content', blank=True)
    submit_time = models.DateTimeField('Time of Submission',
        auto_now_add=True)
    # optional result (TODO: change it to mandatory by adjusting queries)
    result = models.IntegerField('Result', blank=True, null=True)
    def __str__(self):
        return str(self.stu_id)
    def __repr__(self):
        return self.__str__()

               

class Test(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    test_content = models.TextField('Test Content')
    def __str__(self):
        return str(self.ex_id)
    def __repr__(self):
        return self.__str__()


class AssignedExercises(models.Model):
    ex_id = models.ForeignKey('Exercise', to_field='ex_id')
    c_id = models.ForeignKey('Course', to_field='c_id')
    # for setting deadlines (optional)
    deadline = models.DateTimeField("Deadline", blank=True, null=True)
    def __str__(self):
        return self.ex_id.__str__()
    def __repr__(self):
        return self.__str__()

#    def __unicode__(self):
#        return self.c_id.__unicode__() + ' --- ' + self.ex_id.__unicode__()


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
    tch_id = models.ForeignKey('Teacher', to_field = 'user_id')
    students = models.ManyToManyField('Student')
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

 #   def __unicode__(self):
 #       return self.name + ' - Year ' + str(self.year)


class Teacher(models.Model):
    user_id = models.AutoField(primary_key=True)
    uname = models.CharField('Teacher ID', max_length=15, unique=True)
    #name = models.CharField('Name', max_length=50)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    pw = models.CharField('Password', max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.uname
    def __repr__(self):
        return self.__str__()
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
    stu_id = models.ForeignKey('Student', to_field='user_id')
    ex_id  = models.ForeignKey('Exercise', to_field='ex_id')
    score = models.IntegerField('Score', default=0)
    def __str__(self):
        return str(self.stu_id)
    def __repr__(self):
        return self.__str__()

class Student(models.Model):
    user_id = models.AutoField(primary_key=True)
    uname = models.CharField('Student ID', max_length=15, unique=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    # Course has a Many to Many relationship with this, so you can find things
    pw = models.CharField('Password', max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + " " + self.last_name + "(" + str(self.uname) + ")"
    def __repr__(self):
        return self.__str__()
    def __unicode__(self):
        return self.__str__()
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
        
