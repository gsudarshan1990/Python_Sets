"""
Usage of the list comprehension
"""

#Bool of odd numbers % 2 provides true
print(bool(1%2))

#create the lambda function1

odd = lambda x:bool(x%2)
list1 = [n for n in range(10)]
list2 = [n for n in list1 if not odd(n)]
print(list2)

#We should not use the iterable as the default parameter

def function1(bar =[]):
    """
    Problems that occur because of the list iterable acts as a default parameter
    :param bar: empty list
    :return: list
    """
    bar.append('baz')
    return bar

#calling the above function three times
print(function1())#['baz']
print(function1())#['baz', 'baz']
print(function1())#['baz', 'baz', 'baz']

#Please find the example below to resolve the above problem

def function2(bar = None):
    if bar == None:
        bar =[]
    bar.append('baz')
    return bar

print(function2())
print(function2())
print(function2())

