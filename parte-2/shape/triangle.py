"""Definition for the Triangle class"""

from shape.shape import Shape

class Triangle(Shape):
    """A triangle in a 2D space"""

    def __init__(self, side1, side2, side3):

        if not isinstance(side1, (int, float)):
            raise TypeError("side1 must be a number")

        if not isinstance(side2, (int, float)):
            raise TypeError("side2 must be a number")

        if not isinstance(side3, (int, float)):
            raise TypeError("side3 must be a number")

        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def compute_area(self):
        """Compute the area of the triangle using Heron's formula"""
        semiperimeter = self.compute_perimeter() / 2
        return (
            semiperimeter
            * (semiperimeter - self.side1)
            * (semiperimeter - self.side2)
            * (semiperimeter - self.side3)
        ) ** 0.5

    def compute_perimeter(self):
        return self.side1 + self.side2 + self.side3
