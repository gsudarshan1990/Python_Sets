"""
Usage of the multiple exceptions
"""

def function1(inta, intb):
    """
    Divides the two integers
    :param inta: assigns to a
    :param intb: assigns to b
    :return: division of number
    """
    try:
        c =(inta/ intb)
        return c
    except (ArithmeticError,TypeError) as e:
        print(e)

print(function1("ba",0))