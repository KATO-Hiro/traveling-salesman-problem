# vim:fileencoding=utf-8
from math import sqrt


class Point(object):
    """Represents the location of a salesperson."""

    def __init__(self):
        self._x = None
        self._y = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def distance(self, other_point) -> float:
        '''Calculate the distance between a point and the another.'''
        return sqrt((self._x - other_point._x) ** 2 + (self._y - other_point._y) ** 2)
