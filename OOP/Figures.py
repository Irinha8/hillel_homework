from math import pi


class Figure:

    def __init__(self):
        pass

    def perimetr(self):
        pass

    def area(self):
        pass


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def perimetr(self):
        return 2 * pi * self.r

    def area(self):
        return pi * self.r ** 2


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimetr() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5  # площадь треугольника по формуле Герона


class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.a * self.b

