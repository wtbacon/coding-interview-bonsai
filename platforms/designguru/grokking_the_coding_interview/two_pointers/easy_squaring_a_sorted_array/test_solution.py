from .solution import Solution


def test1():
    s = Solution()
    assert s.makeSquares([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]


def test2():
    s = Solution()
    assert s.makeSquares([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]
