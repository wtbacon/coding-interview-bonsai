from .solution import Solution


def test_1():
    s = Solution()
    assert s.numGoodPairs([1, 2, 3, 1, 1, 3]) == 4


def test_2():
    s = Solution()
    assert s.numGoodPairs([1, 1, 1, 1]) == 6


def test_3():
    s = Solution()
    assert s.numGoodPairs([1, 2, 3]) == 0
