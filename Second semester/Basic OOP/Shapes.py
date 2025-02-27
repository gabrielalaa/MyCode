from math import pi, sqrt

class Shape:
    def __init__(self, name):
        self.name = name

        self.area = None
        self.perimeter = None


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

        self.calculate(self.radius)

    def calculate(self, radius):
        self.area = pi * (radius ** 2)
        self.perimeter = 2 * pi * radius
        print(f"Area of Circle: {self.area.__round__(2)}. Perimeter of Circle: {self.perimeter.__round__(2)}")


class Triangle(Shape):
    def __init__(self, name, l):
        super().__init__(name)
        self.l = l

        self.calculate(self.l)

    def calculate(self, l):
        self.area = ((l**2) * sqrt(3))/4
        self.perimeter = 3 * l
        print(f"Area of Triangle: {self.area.__round__(2)}. Perimeter of Triangle: {self.perimeter.__round__(2)}")


class Square(Shape):
    def __init__(self, name, l):
        super().__init__(name)
        self.l = l

        self.calculate(self.l)

    def calculate(self, l):
        self.area = l ** 2
        self.perimeter = l * 4
        print(f"Area of Square: {self.area.__round__(2)}. Perimeter of Square: {self.perimeter.__round__(2)}")


c1 = Circle('Circle', 2)
t1 = Triangle('Triangle', 3)
s1 = Square('Square', 4)