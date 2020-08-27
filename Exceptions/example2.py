"""
This is the second example of exception
"""

students =[('Timmy', 95, 'Will Pass'), ('Martha', 70), ('Betty', 82,'Will Pass'), ('Stewart', 50, 'Will Not Pass'), ('Ashley', 68),
           ('Natalie', 99, 'Will Pass') ,('Archie', 71), ('Carl', 45, 'Will not pass')]

passing ={'Will Pass' : 0 , 'Will Not Pass': 0}
for student in students:
    try:
        if student[2] == 'Will Pass':
            passing['Will Pass']+=1
        elif student[2] == 'Will Not Pass':
            passing['Will Not Pass']+=1
    except IndexError:
        print('Index Out of range exception')

print(passing)



