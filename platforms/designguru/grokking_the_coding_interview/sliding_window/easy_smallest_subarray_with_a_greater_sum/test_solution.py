from .solution import Solution


def test1():
    s = Solution()
    assert s.findMinSubArray(7, [2, 1, 5, 2, 3, 2]) == 2


def test2():
    s = Solution()
    assert s.findMinSubArray(7, [2, 1, 5, 2, 8]) == 1


def test3():
    s = Solution()
    assert s.findMinSubArray(8, [3, 4, 1, 1, 6]) == 3
