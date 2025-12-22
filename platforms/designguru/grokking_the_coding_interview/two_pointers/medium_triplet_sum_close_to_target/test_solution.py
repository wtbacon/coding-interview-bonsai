from .solution import Solution


def test1():
    s = Solution()
    assert s.searchTriplet([0, 0, 1, 1, 2, 6], 5) == 4


def test2():
    s = Solution()
    assert s.searchTriplet([-1, 0, 2, 3], 3) == 2


def test3():
    s = Solution()
    assert s.searchTriplet([-3, -1, 1, 2], 1) == 0


def test4():
    s = Solution()
    assert s.searchTriplet([1, 0, 1, 1], 100) == 3


def test5():
    s = Solution()
    assert s.searchTriplet([-1, -1, 1, 1, 2], 1) == 1