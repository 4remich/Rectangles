class Rectangle:

    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.square() + other.square()
        if isinstance(other, int | float):
            return self.square() + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.square() + other
        return NotImplemented

    def __mul__(self, other):
        return self.square() * n

    def __str__(self):
        return f'{self.a} * {self.b}'



a = Rectangle(5, 4)
b = Rectangle(3, 7)
n = 3


print(a)
print(b)
print(a * n)
print(a + b)
