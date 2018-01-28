# vim:fileencoding=utf-8
from math import sqrt


class Point(object):
    """Represents the location of a salesperson."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point) -> float:
        '''Calculate the distance between a point and the another.'''
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
