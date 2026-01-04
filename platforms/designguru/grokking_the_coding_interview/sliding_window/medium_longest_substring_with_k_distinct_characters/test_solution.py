from .solution import Solution


def test1():
    s = Solution()
    assert s.findLength("araaci", 2) == 4


def test2():
    s = Solution()
    assert s.findLength("araaci", 1) == 2


def test3():
    s = Solution()
    assert s.findLength("cbbebi", 3) == 5
