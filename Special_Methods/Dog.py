class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f'name of the dog is {self.name} and breed of the dog is {self.breed}'

d1=Dog('jimmy',"alscesion")
print(d1)

