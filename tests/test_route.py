# vim:fileencoding=utf-8
from src.mypkg.route import Route


class TestRoute(object):

    def test_add(self):
        route = Route()
        point = route.add_point(name='1', x=3, y=5)

        assert len(route._points) == 1
        assert 3 == point.x
        assert 5 == point.y
