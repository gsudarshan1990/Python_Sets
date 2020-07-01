class classroom:
    """Description about the students in the class"""
    def __init__(self, code, max_number_students):
        self.code = code
        self.max_number_students = max_number_students
        self.students = {}

    def add_student(self,student):
        if len(self.students) < self.max_number_students:
            self.students[student.name] = student.grade

    def delete_student(self,student):
        del self.students[student.name]

    def __getitem__(self,student_name):
        return self.students[student_name]
class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

s1=Student("John",29,'A')
s2=Student("Jackson",30,'B')
s3=Student("Johnny",35,'B')

c1=classroom("F2",10)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)

print(c1.students)
print(c1["Jackson"])