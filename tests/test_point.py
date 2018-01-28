# vim:fileencoding=utf-8
from src.mypkg.point import Point


class TestPoint(object):

    def test_init(self):
        point = Point(x=3, y=5)
        assert 3 == point.x
        assert 5 == point.y

    def test_distance(self):
        start_point = Point(x=1, y=1)
        end_point = Point(x=4, y=5)

        distance = end_point.distance(start_point)
        assert 5.0 == distance
