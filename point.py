import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_polar(self):
        return math.sqrt(self.x ** 2 + self.y ** 2), math.atan(self.y / self.x)


"""
point1 = Point(int(input()), int(input()))
print(point1.to_polar())
"""
