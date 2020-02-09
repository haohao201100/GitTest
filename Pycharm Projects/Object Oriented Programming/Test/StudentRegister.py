class Student:
    population = 0

    def __init__(self, name, age, cls):
        self.name = name
        print("(Initializing{})".format(self.name))

        Student.population += 1

    def transfer(self):
        print("{} is being Register!".format(self.name))

        Student.population -= 1

        if Student.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} Student Remaining.".format(
                Student.population))

    def greeting(self):

        print("Greetings, the student{}.".format(self.name))

    def how_many(cls):
        print("We have {:d} Student.".format(cls.population))


student1 = Student("MgMg", 14, 'Bio')
student1.transfer()
student1.how_many()

student2 = Student("MaNi", 13, 'Eco')
student2.transfer()
student2.how_many()

student3 = Student("HlaHla", 12, 'Eco')
student3.transfer()
student3.how_many()

print("Student are all Register")
student1.transfer()
student2.transfer()
student3.transfer()
