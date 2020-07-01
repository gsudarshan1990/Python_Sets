class School:
    """Describes about the student"""
    def __init__(self, students, grades):
        """
        Initializes the parameter
        :param students: list of students
        :param grades: grade of students
        """
        self.students=students
        self.grades = grades

    def __getitem__(self, number):
        """returns the student grade"""
        return self.grades[number]

    def __setitem__(self, i,grade):
        self.grades[i]=grade


class student:
    def __init__(self, number, name):
        self.number = number
        self.name = name

students=[student(1,"sonu"),student(2,"shashank"),student(3,"deepu")]
grades=['A+','A-','B+']
school=School(students,grades)
print(school[1])
school[2]='A'
print(school[2])
print(id(school))
print(school)
print(hex(id(school)))