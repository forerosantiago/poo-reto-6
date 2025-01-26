"""Line class definition"""

from shape.point import Point

class Line:
    """A line in a 2D space"""

    def __init__(self, start_point: "Point", end_point: "Point"):

        if not isinstance(start_point, Point):
            raise TypeError("start_point must be a Point object")

        if not isinstance(end_point, Point):
            raise TypeError("end_point must be a Point object")

        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self) -> float:
        """Compute the length of the line"""
        return self.start_point.compute_distance(self.end_point)
