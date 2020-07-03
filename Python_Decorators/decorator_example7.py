def outer_decorator(function1):
    """This is the outer decorator"""
    def inner_decorator():
        """This is the inner decorator"""
        print("Before the function1 is called {}".format(function1.__name__))
        function1()
        print("After the function1 is called {}".format(function1.__name__))
    return inner_decorator

@outer_decorator
def wrap_me():
    print("This is the wrap function")

wrap_me()