

def outer_decorator(function1):
    def inner_decorator():
        print("Welcome to Solar System")
        function1()
    return inner_decorator

@outer_decorator
def greeting():
    print("Hello world")

greeting()