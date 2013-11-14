class AssignmentsBook:
	def __init__(self, chapters):
		self.chapters = chapters
	# def __repr__(self):
	# 	return self.__str__(self)
	def get_chapters(self):
		return self.chapters
	# def __str__(self):
	# 	rep = ""
	# 	for chapter in self.chapters:
	# 		rep += str(chapter)
	# 	return rep
		

class Chapter:
	def __init__(self, name, assignments):
		self.name = name
		self.assignments = assignments
	def get_name(self):
		return self.name
	def get_assignments(self):
		return self.assignments
	# def __repr__(self):
	# 	return self.__str__(self)
	# def __str__(self):
	# 	rep = "Chapter: " + str(self.name) + ": \n"
	# 	for assingment in self.assignments:
	# 		rep += "\t" + str(assingment)
	# 	return rep

class Assignment:
	def __init__(self, name, id, code=None, description=None):
		self.name = name
		self.id = id
		self.code = code
		self.description = description
	def get_name(self):
		return self.name
	def get_id(self):
		return self.id
	def get_description(self):
		return self.description
	def get_code(self):
		return self.code
	# def __repr__(self):
	# 	return self.__str__(self)
	def set_code(self, code):
		self.code = code
	# def __str__(self):
	# 	return "{ Assignment: " + self.name + ": , id:" + self.id + "}"