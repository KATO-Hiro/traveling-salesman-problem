# vim:fileencoding=utf-8
from src.mypkg.point import Point


class TestPoint(object):

    def test_init(self):
        point = Point(x=3, y=5)
        assert 3 == point.x
        assert 5 == point.y
