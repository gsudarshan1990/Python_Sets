class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __len__(self):
        return round((self.x**2+self.y**2)**(1/2))

p1=Point(10,20)
print(len(p1))