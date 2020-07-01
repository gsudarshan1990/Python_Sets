class Student:
    """
    Class describing about each student
    """
    def __init__(self, number, name):
        """
        Initializes the instance variables
        :param number: id of the student
        :param name: name of the student
        """
        self.number = number
        self.name = name

class school:
    """
    Total number of students in the school
    """
    def __init__(self, students, grades):
        """
        Initializes the student
        :param students: Instance of the student
        :param grades: grade of the student
        """
        self.students = students
        self.grades = grades

    def __len__(self):
        """
        :return: total number of students
        """
        return len(self.grades)

students1=[(1,"John"),(2,"Selvia"),(3,"Botham")]
grades1=['A+','A-','B+']
sc=school(students1,grades1)
print(len(sc))