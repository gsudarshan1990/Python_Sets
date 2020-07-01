class Point4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return f'x-{x} and y-{y}'
p1=Point4(10,25)
p2=Point4(16,12)
p3=p1-p2
print(p3)