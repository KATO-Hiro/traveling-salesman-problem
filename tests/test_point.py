# vim:fileencoding=utf-8
from src.mypkg.point import Point


class TestPoint(object):

    def test_init(self):
        point = Point()
        point.x = 3
        point.y = 5
        assert 3 == point.x
        assert 5 == point.y

    def test_distance(self):
        start_point = Point()
        start_point.x = 1
        start_point.y = 1
        end_point = Point()
        end_point.x = 4
        end_point.y = 5

        distance = end_point.distance(start_point)
        assert 5.0 == distance
