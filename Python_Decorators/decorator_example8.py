def outer_decorator(function1):
    """This is the outer decorator"""
    def inner_decorator(*args, **kwargs):
        """
        This is the inner decorator and takes two argument
        :param args: Positional arguements
        :param kwargs: keyword arguments
        :return:
        """
        print(f'{args},{kwargs}')
        function1()
    return inner_decorator

@outer_decorator
def wrapper_fuction():
    print("Arguments passed")

wrapper_fuction()
wrapper_fuction(10, 20)
wrapper_fuction(15, course = "decorator",subject ="Python" )