divide=lambda x,y:x/y
print(divide(3,6))

triple=lambda x:x*3
print(triple(5))

square=lambda x:x**2
print(square(5))

cube = lambda x:x**3
print(cube(9))

#lambda with iterable
pets=['dog','turtle','bird','fish','kitty']
pets2=sorted(pets,key=lambda x:len(x))
print(pets2)
pet3=sorted(pets,key=lambda x:len(x),reverse=True)
print(pet3)

grades =[{'name':'Jennifer','final':95},{'name':'David','final':92},{'name':'Aaron','final':98}]
grades2=sorted(grades,key=lambda x:x['final'])
grades3=sorted(grades,key=lambda x:x['name'])
print('Based on marks')
print(grades2)
print('Based on name')
print(grades3)

grades = [{'name':'Jennifer','final':95},{'name':'David','final':92},{'name':'Aaron','final':98}]
max_value=max(grades,key=lambda x:x['final'])
min_value=min(grades,key=lambda x:x['final'])
print(min_value)
print(max_value)