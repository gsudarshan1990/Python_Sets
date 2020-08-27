"""
This is the third example of exception
"""

d1 ={'a':1, 'b':2, 'c':3, 'd':4}

try:
    d1['f']
except KeyError:
    print('Key is not found')