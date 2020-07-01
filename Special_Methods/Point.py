class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x-{self.x} and y-{self.y}'

p1=Point(56,60)
print(p1)