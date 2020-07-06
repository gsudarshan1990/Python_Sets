"""
This is the example of the decorators function
"""
from functools import reduce


def outer_decorator(function1):
    """This is the outer decorator"""
    def inner_decorator(*args, **kwargs):
        """This is the inner decorator"""
        print("The current function is called ", function1.__name__)
        function1(*args,**kwargs)
    return inner_decorator

@outer_decorator
def calculator(a,b):
    """This is the calculator function"""
    print(f'adding a,b {a+b} and substracting a,b {a-b}')

calculator(10,20)

@outer_decorator
def calculator2(*args):
    """ This is the second function1"""
    print(reduce(lambda a,b:a+b, args))
    print(reduce(lambda a,b:a-b, args))

calculator2(15,20,35,55,114)