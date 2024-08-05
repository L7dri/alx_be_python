import math

class Shape:
    """Base class for different shapes."""
    def area(self):
        raise NotImplementedError("Subclasses must override area() method")


class Rectangle(Shape):
    """Class representing a rectangle, inherits from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    """Class representing a circle, inherits from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
