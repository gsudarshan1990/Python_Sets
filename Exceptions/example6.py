"""
This is the another index error example
"""

foods =['chocolate','chicken','corn','sandwich','soup','potatoes','beef','lox','lemonade']

print('Appending the fifth letter of each food')

fourth_letter=[]

for food in foods:
    try:
        fourth_letter.append(food[4])
    except IndexError:
        print('Index Error')

print(fourth_letter)
