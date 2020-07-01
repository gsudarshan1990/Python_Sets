def outer_decorator1(function1):
    """This is the decorator function which return wrapper function and takes function as argument"""
    def inner_decorator():
        """This is the inner decorator where outer function argument is executed"""
        print("Hello Solar System")
        function1()
    return inner_decorator

def outer_decorator2(function1):
    """This is the outer decorator which takes function as argument and returns another function"""
    def inner_decorator():
        print("Welcome to the Galaxy system")
        function1()
    return inner_decorator

@outer_decorator1
@outer_decorator2
def greeting():
    print("Hello World")

greeting()