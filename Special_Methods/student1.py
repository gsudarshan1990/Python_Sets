class Student:
    def __init__(self,name,age,gps,id_):
        self.name = name
        self.age = age
        self.gps = gps
        self.id = id_

    def __str__(self):
        return f'name:{self.name} , age :{self.age}, gps:{self.gps} and id:{self.id}'

s1=Student("sonu",15,10,'SUN1')
print(s1)