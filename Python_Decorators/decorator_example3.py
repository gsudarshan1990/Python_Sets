def outer_decorator(function1):
    """This is the outer decorator takes function as arugment and return new function"""
    def inner_decorator():
        """This is the inner decorator where the outer function argument is executed"""
        print("Welcome to Galaxy system")
        function1()
    return inner_decorator

@outer_decorator
def greeting():
    print("Hello world")

greeting()