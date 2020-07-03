"""
Creation of the dictionaries with the help of the dict() constructor
"""

#Usage of the tuple for creating the dictionary
tuple1=(('a',0),('b',1),('c',2))
dict1 =dict(tuple1)
print(dict1)

#Usage of two iterables to create the dictionary
list1 = ['spanish','french','German']
list2 = ['Argentina','France','Germany']
dict1=dict(zip(list1,list2))
print(dict1)

#usage of the assignment operator to create the dictionary
dict1 = dict(a=0, b=1, c=2, d=3)
print(dict1)