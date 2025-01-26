"""Definition for the Square class"""

from shape.rectangle import Rectangle


class Square(Rectangle):
    """A square in a 2D space"""

    def __init__(self, side):

        if not isinstance(side, (int, float)):
            raise TypeError("side must be a number")

        super().__init__(side, side)
