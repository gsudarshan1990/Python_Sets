"""
This is the example which explains about the iterable and the iterator
"""

my_list =[1,2,3,4,5]
print(type(my_list))

my_list_iterator = iter(my_list)
print(type(my_list_iterator))


from collections.abc import Iterator, Iterable

print(isinstance(my_list,Iterable))
print(isinstance(my_list_iterator,Iterator))