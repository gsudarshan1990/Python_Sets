def outer_decorator1(function1):
    """This is the outer decorator and takes function as the arugment and returns the wrapper function"""
    def inner_decorator(planet=None):
        """This is the inner decorator which takes one argument"""
        if planet:
            print("Hello"+planet)
            function1()
        else:
            print("Hello world")
            function1()
    return inner_decorator

@outer_decorator1
def greeting(planet=None):
    """This is the function which needs to be decorated"""
    print("Welcome to the galaxy system")

greeting()
greeting("Mars")