class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return (self.x + other.x), (self.y + other.y)

    def __sub__(self, other):
        return (self.x - other.x), (self.y - other.y)

    def __mul__(self, other):
        return (self.x * other), (self.y * other)


"""
v1 = Vector(int(input("Введите координату x1: ")), int(input("Введите координату y1: ")))
v2 = Vector(int(input("Введите координату x2: ")), int(input("Введите координату y2: ")))

k = int(input("Введите число:"))
print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1 * k)
"""
