"""
Usage of the list and the lambda function
"""

odd = lambda x: bool(x%2)
list1=[n for n in range(10)]
list2=[x for x in list1 if not odd(x)]
print(list2)

#Iterables should not be declared as a default argument
def function1(bar=[]):
    bar.append('baz')
    return bar

print(function1())
print(function1())
print(function1())

#Implementation of the above method
def function2(bar = None):
    if bar ==None:
        bar=[]
    bar.append('baz')
    return bar

print(function2())
print(function2())
print(function2())
