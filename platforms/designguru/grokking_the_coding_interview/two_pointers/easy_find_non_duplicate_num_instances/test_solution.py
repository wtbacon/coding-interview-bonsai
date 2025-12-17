from .solution import Solution


def test_1():
    s = Solution()
    assert s.moveElements([2, 3, 3, 3, 6, 9, 9]) == 4
