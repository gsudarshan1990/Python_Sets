def dump_args_outer_decorator(function1):
    """
    This is the outer decorator
    :param function1: Takes the function as the argument
    :return: returns another function as the argument
    """
    def inner_decorator(*args, **kwargs):
        """
        This is the inner decorator
        :param args: takes the positional argument
        :param kwargs: takes the keyword argument
        :return:
        """
        print(f'{function1.__name__}, {args} {kwargs}')
        function1(*args, **kwargs)
    return inner_decorator

import datetime
def cal_time_outer_decorator(function1):
    """
    This is the outer decorator
    :param function1: Takes the function as the argument
    :return: returns the functions
    """
    def inner_decorator(*args, **kwargs):
        """
        This is the inner decorator
        :param args: Takes the positional argument
        :param kwargs: Takes the Keyword argument
        :return:
        """
        time1 = datetime.datetime.now()
        print("Start time is :", time1.strftime("%D/%M/%Y %H:%M:%S"))
        function1(*args, **kwargs)
        time2 = datetime.datetime.now()
        print("End time is : ", time2.strftime("%D/%M%Y %H:%M:%S"))
    return inner_decorator

@dump_args_outer_decorator
@cal_time_outer_decorator
def decorated_function(*args,**kwargs):
    """
    The function which utilizes the decorator
    :param args: Takes the positional argument
    :param kwargs: Takes the Keyword argument
    :return: returns nothing
    """
    print(*args)
    for key,value in kwargs.items():
        print(key, value)


decorated_function(1,2,3,4,course = "Biology",  Subject ="Physics" , height =20)
