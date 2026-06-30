from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side


my_circle = Circle(17)
print(f"Circle Area: {my_circle.calculate_area()}")
print(f"Circle Perimeter: {my_circle.calculate_perimeter()}")

my_rectangle = Rectangle(5, 8)
print(f"Rectangle Area: {my_rectangle.calculate_area()}")
print(f"Rectangle Perimeter: {my_rectangle.calculate_perimeter()}")

my_square = Square(7)
print(f"Square Area: {my_square.calculate_area()}")
print(f"Square Perimeter: {my_square.calculate_perimeter()}")
