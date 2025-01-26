"""Definition of the Point class"""

import math


class Point:
    """A point in a 2D space"""

    def __init__(self, x: float, y: float):

        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")

        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")

        self.x = x
        self.y = y

    def compute_distance(self, other_point: "Point") -> float:
        """Compute the distance between two points"""

        if not isinstance(other_point, Point):
            raise TypeError("other_point must be a Point object")

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
