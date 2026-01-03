from .solution import Solution


def test1():
    s = Solution()
    assert s.findMaxSumSubArray(3, [2, 1, 5, 1, 3, 2]) == 9


def test2():
    s = Solution()
    assert s.findMaxSumSubArray(2, [2, 3, 4, 1, 5]) == 7
