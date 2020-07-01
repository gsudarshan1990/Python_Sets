#enumerate example
students=['John','Aaron','Jennifer','Ashley']
for index,name in enumerate(students):
    print(index,": "+name)

print('Using the reversed function')
#reversed
for index,name in enumerate(reversed(students)):
    print(index,": "+name)

print("Usage of the zip function")
#zip
students=['John','Aaron','Jennifer','Ashley']
scores=[90,99,102,104]


for index,student_result in enumerate(zip(students,scores)):
    student,result=student_result
    print(index,": "+student+"-"+str(result))