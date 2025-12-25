from .solution import Solution


def test1():
    s = Solution()
    assert s.searchTriplets([-1, 0, 2, 3], 3) == 2


def test2():
    s = Solution()
    assert s.searchTriplets([-1, 4, 2, 1, 3], 5) == 4
