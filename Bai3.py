import math
from Bai2 import Shape

class Circle(Shape):

    def __init__(self, x, y, bankinh):
        super().__init__(self, x, y)
        self.bankinh = bankinh

    def chuvi(self):
        return self.bankinh*3.14

    def dientich(self):
        return (2*self.bankinh*3.14) / 4

class Rect(Shape):

    def __init__(self, x, y, dai, rong):
        super().__init__(self, x, y)
        self.dai = dai
        self.rong = rong

    def chuvi(self):
        return (self.dai+self.rong) * 2

    def dientich(self):
        return self.dai*  self.rong



class Triangle(Shape):

    def __init__(self, x, y, a, b, c):
        super().__init__(self, x, y)
        self.a = a
        self.b = b
        self.c = c

    def chuvi(self):
        return self.a + self.b + self.c

    def dientich(self):
        return math.sqrt((self.chuvi() / 2)*((self.chuvi()/2)-self.a)*((self.chuvi()/2)-self.b)*((self.chuvi()/2)-self.c))