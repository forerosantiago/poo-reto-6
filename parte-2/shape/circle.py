"""Circle class module"""

import math

from shape.shape import Shape


class Circle(Shape):
    """A circle in a 2D space"""

    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        super().__init__()
        self.radius = radius

    def compute_area(self):
        """Compute the area of the circle"""
        return math.pi * self.radius**2

    def compute_perimeter(self):
        """Compute the perimeter of the circle"""
        return 2 * math.pi * self.radius
