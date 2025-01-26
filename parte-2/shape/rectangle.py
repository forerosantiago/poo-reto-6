"""Definition for the Rectangle class"""

from shape.shape import Shape


class Rectangle(Shape):
    """A rectangle in a 2D space"""

    def __init__(self, width, height):

        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")

        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")

        super().__init__()
        self.width = width
        self.height = height

    def compute_area(self) -> float:
        return self.width * self.height

    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)
