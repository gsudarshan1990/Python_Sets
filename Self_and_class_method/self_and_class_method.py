"""
Usage of the self and class method
"""

class Student:
    """
    Class describes about the Student
    """
    def greet(self, name):
        print("Hello", name)

student = Student()
student.greet('John')
print('*'*20)
class Student:
    """
    Class describes about the student with its identity
    """
    def greet(self, name):
        print(id(self))
        print('Hello', name)

student = Student()
student.greet('Gaddar')

#Usage of the class method
class Student:
    """
    This class provides information about the student along with the usage of the class method
    """
    def __init__(self, name):
        self.name = name

    @classmethod
    def class_method(cls, first_name, second_name):
        return cls(first_name+' '+second_name)

s1=Student.class_method('John','Smith')
print(s1.name)