class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return f'x-{x} and y-{y}'

p1=Point(25,30)
p2=Point(15,5)
p3=p1-p2
print(p3)
