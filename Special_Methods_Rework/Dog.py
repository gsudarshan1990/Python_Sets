class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f'name - {self.name} age -{self.age} breed-{self.breed}'

d1=Dog("johnson",10,"snipper")
print(d1)