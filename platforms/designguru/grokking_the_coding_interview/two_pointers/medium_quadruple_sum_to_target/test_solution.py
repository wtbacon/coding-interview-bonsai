from .solution import Solution


def test1():
    s = Solution()
    assert s.searchQuadruplets([4, 1, 2, -1, 1, -3], target=1) == [[-3, -1, 1, 4], [-3, 1, 1, 2]]


def test2():
    s = Solution()
    assert s.searchQuadruplets([2, 0, -1, 1, -2, 2], target=2) == [[-2, 0, 2, 2], [-1, 0, 1, 2]]
