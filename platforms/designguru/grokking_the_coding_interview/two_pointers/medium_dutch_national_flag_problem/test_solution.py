from .solution import Solution


def test1():
    s = Solution()
    assert s.sort([1, 0, 2, 1, 0]) == [0, 0, 1, 1, 2]


def test2():
    s = Solution()
    assert s.sort([2, 2, 0, 1, 2, 0]) == [0, 0, 1, 2, 2, 2]


def test3():
    s = Solution()
    assert s.sort([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
