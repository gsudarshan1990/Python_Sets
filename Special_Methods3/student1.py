class Student:
    def __init__(self, name, favorite_subject,age):
        self.name = name
        self.age = age
        self.favorite_subject = favorite_subject

    def __str__(self):
        return f"name :{self.name} age:{self.age} favorite_subject:{self.favorite_subject}"

s1=Student("sonu","physics",15)
print(s1)