"""
This is the first doc string example
"""

def power(a, b):
    """
    Returns a to the power of b
    :param a: arg1 and int type
    :param b: arg2 and int type
    :return: returns the int type value
    """
    return a**b

print(power(10,5))

def multiply(a, b, c=0):
    """
    Provides the multiplication of the three numbers
    :param a: arg1 and int type
    :param b: arg2 and int type
    :param c: arg3 and int type
    :return: multiplication of three numbers
    """
    if a == b:
        raise ValueError("arg1 and arg2 should not be equal")

    return a*b*c

print(multiply(10,5,12))