# vim:fileencoding=utf-8
from src.mypkg.point import Point


class Route(object):
    """Represents a salesperson's route."""

    def __init__(self):
        self._points = dict()

    def add_point(self, name, x, y):
        if name not in self._points:
            self._points[name] = Point(x, y)
        return self._points[name]
