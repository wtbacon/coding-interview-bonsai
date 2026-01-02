from .solution import Solution


def test1():
    s = Solution()
    assert s.loopExists([1, 2, -1, 2, 2]) is True


def test2():
    s = Solution()
    assert s.loopExists([2, 2, -1, 2]) is True


def test3():
    s = Solution()
    assert s.loopExists([2, 1, -1, -2]) is False


def test4():
    s = Solution()
    assert s.loopExists([3, 2, -2, 5, 6]) is False
