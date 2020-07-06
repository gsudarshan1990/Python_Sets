#Example of the employees

employees =['John','Johnson','James']

for index, employee in enumerate(employees,start =3001):
    print(str(index)+":"+employee)

print("========usage of reversed=====")

meals =['poori', 'dosa', 'idly', 'upma', 'kichidi']

for meal in reversed(meals):
    print(meal)

print("In the form of employees")

class Employee:
    """
    This class describes about the employee
    """
    def __init__(self, name, score):
        """
        Initializing the values
        :param name: assigning to name
        :param score: assigning to score
        """
        self.name = name
        self.score = score

    def __repr__(self):
        """Representation in the form of string"""
        return f"Employee({self.name},{self.score})"

employee0 = Employee('John',91)
employee1 = Employee('Jacob',87)
employee3 = Employee('Watson', 94)
employee4 = Employee('Anderson', 95)

List_Employees =[employee0, employee1, employee3, employee4]

for employee in sorted(List_Employees,key= lambda x:x.score, reverse =True):
    print(employee)

print("Using the zip function")

print()
print()
#Usage of the zip function
numbers0 = [15, 20, 12]
numbers1 = [5, 8, 15]

for num0, num1 in zip(numbers0, numbers1):
    print(f'{num0} * {num1} = {num0 * num1}')

#Second example of zip

print("")

letters0 = ['a', 'b', 'c', 'd']
letters1 = ['z', 'x','y', 't']

list_ =list()

for let0,let1 in zip(letters0,letters1):
    list_.append((let0,let1))

print(list_)


