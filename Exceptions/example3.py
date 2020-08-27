"""
This is the third example of exception
"""

numbers = [5, 9 ,'4', 3, 2, 1 ,6 , 5 , '7', 4, 3, 2 , 6, 7, 8, '0', 3, 4, 0 , 6, 5 , '3', '1' , 5, 6, 9 , 3, 2, 5, 6, '9', 2, 3, 4,5 ,1]

plus_four = []
for num in numbers:
    try:
        plus_four.append(num+4)
    except TypeError:
        plus_four.append('Error')

print(plus_four)
