"""
Explaining the fibonacci series in the form of the class object
"""

class Fibonacci:
    """
    This is the class which explains the fibonacci series
    """
    def __init__(self):
        """
        Initializing the values
        """
        self.a =0
        self.b =1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b , self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a

f=Fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))