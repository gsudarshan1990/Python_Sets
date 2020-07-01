def outer_decorator(function1):
    def inner_decorator():
        print(f'Before calling the funciton {function1.__name__}')
        function1()
        print(f'After calling the function {function1.__name__}')
    return inner_decorator

@outer_decorator
def say_hello():
    print('hello world')

say_hello()