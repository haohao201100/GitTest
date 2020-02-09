class SchoolMember:
	'''Represents any school member.'''

	def_init_(self, name, age):
		self.name = name
		self.age = age
		print('Initialized SchoolMember: {})'.format(self.name))

	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age),end="")

class Teacher(SchoolMember):
	'''Represents a student.'''

	def_init_(self, name, age, marks):
		SchoolMember._init_(self, name, age)
		self.marks = marks
		print('(Initialized Student:{})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'format(self.marks))

class Student(SchoolMember):
	'''Represents a Student'''

	def_init_(self, name, age marks):
		SchoolMember._init_(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks:  "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()


members = [t,s]
for member in members:
	member.tell()