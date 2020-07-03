"""
Usage of the dictionary comprehension
"""

squares ={x:x**x for x in range(5)}
print(squares)

odd_squares = {x:x**2 for x in range(10) if x%2 == 1}
print(odd_squares)