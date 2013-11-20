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
	def __init__(self, name, id=-1, assignments=None):
		self.name = name
		self.id = id
		self.assignments = assignments
	def get_assignments(self):
		return self.assignments
	def get_id(self):
		return self.id
	def get_name(self):
		return self.name
