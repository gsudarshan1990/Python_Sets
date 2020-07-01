class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return f'x-{x} y-{y}'

p1=Point(10,20)
p2=Point(25,30)
p3=p1+p2
print(p3)