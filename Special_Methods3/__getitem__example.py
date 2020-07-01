class classroom:
    """Describes about the classroom"""
    def __init__(self, code, max_students):
        """
        Initializes the variables
        :param code: code of the class room
        :param name: name of the class room
        """
        self.code = code
        self.max_students = max_students
        self.students={}

    def add_student(self, student):
        """
         Adds the student
        :param student: instance of student
        :return: No return
        """
        if len(self.students) < self.max_students:
            self.students[student.name]=student.grades

    def remove_student(self, student):
        """
        removes student
        :param student:instance of the student
        :return: No return
        """
        del self.students[student.name]

    def __getitem__(self, student_name):
        """
        provides the grade of the student
        :param student_name: takes the name of the student
        :return:
        """
        return self.students[student_name]

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

s1=Student("Sonu",29,(98,99,89))
s2=Student("Deepu",29,(90,87,66))
s3=Student("rahul",27,(90,90,90))

c1=classroom("Bio",10)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(c1["Sonu"])