from .solution import Solution


def test1():
    s = Solution()
    assert s.findLength([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6


def test2():
    s = Solution()
    assert s.findLength([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9


def test3():
    s = Solution()
    assert s.findLength([1, 0, 0, 1, 1, 0, 1, 1], 2) == 6
