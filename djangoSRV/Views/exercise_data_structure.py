class AssignmentsBook:
	def __init__(self, chapters):
		self.chapters = chapters

	def get_chapters(self):
		return self.chapters

class Chapter:
	def __init__(self, name, assignments):
		self.name = name
		self.assignments = assignments
	def get_name(self):
		return self.name
	def get_assignments(self):
		return self.assignments

class Assignment:
	def __init__(self, name, id):
		self.name = name
		self.id = id
	def get_name(self):
		return self.name
	def get_id(self):
		return self.id


