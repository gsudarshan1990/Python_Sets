"""
This is the first example of exception
"""

try:
    items =['a','b']
    b = items[2]
    print('Can this be printed?')
except IndexError:
    print('Index cannot be calculated')
print('Continuing')

print('This is the second example')

try:
    items =['a','b']
    b = items[2]
    print('Can this be printed?')
except Exception as e:
    print('Got the error')
    print(e)