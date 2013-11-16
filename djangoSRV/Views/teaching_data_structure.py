class TeachingHierarchy:
	def __init__(self, year):
		self.year = year
	def get_teaching_years(self):
		return self.year

class SchoolYear:
	def __init__(self, name, classes):
		self.name = name
		self.classes =  classes
	def get_teaching_classes(self):
		return self.classes
	def get_name(self):
		return self.name

class TeachingClass:
	def __init__(self, name, id=-1, students_data=None):
		self.name = name
		self.students_data = students_data
		self.id = id
	def get_id(self):
		return self.id
	def get_name(self):
		return self.name
	def get_students_data(self):
		return self.students_data

class StudentData:
	def __init__(self, index, chapter, problem_name, student_name, grade):
		self.index=index
		self.chapter = chapter
		self.problem_name = problem_name
		self.student_name = student_name
		self.grade = grade
	def get_index(self):
		return self.index
	def get_chapter(self):
		return self.chapter
	def get_problem_name(self):
		return self.problem_name
	def get_student_name(self):
		return self.student_name
	def get_grade(self):
		return self.grade

