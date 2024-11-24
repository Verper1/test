from math import pi


class Init:
    def __init__(self):
        self.x = int(input('Введите число: '))
        self.p = pi


class Circle(Init):
    def __init__(self):
        super().__init__()

    def get_s(self):
        return print((self.x ** 2) * self.p)


class Square(Init):
    def __init__(self):
        super().__init__()

    def get_s(self):
        return print(self.x ** 2)


class Rectangle(Init):
    def __init__(self):
        super().__init__()
        self.b = int(input('Введите второе число: '))

    def get_s(self):
        return print(self.x * self.b)

c1 = Circle()
c1.get_s()

s1 = Square()
s1.get_s()

r1 = Rectangle()
r1.get_s()
