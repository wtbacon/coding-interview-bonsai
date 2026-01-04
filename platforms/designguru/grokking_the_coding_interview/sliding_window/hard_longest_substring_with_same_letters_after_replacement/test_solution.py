from .solution import Solution


def test1():
    s = Solution()
    assert s.findLength("aabccbb", 2) == 5


def test2():
    s = Solution()
    assert s.findLength("abbcb", 1) == 4


def test3():
    s = Solution()
    assert s.findLength("abccde", 1) == 3
