from .solution import Solution


def test1():
    s = Solution()
    assert s.findLength(["A", "B", "C", "A", "C"]) == 3


def test2():
    s = Solution()
    assert s.findLength(["A", "B", "C", "B", "B", "C"]) == 5


def test3():
    s = Solution()
    assert s.findLength(["A", "B", "B", "A", "C", "C", "C", "A", "A"]) == 6
