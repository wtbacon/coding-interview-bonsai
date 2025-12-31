from .solution import Solution


def test1():
    s = Solution()
    assert s.find(12) is False


def test2():
    s = Solution()
    assert s.find(23) is True


def test3():
    s = Solution()
    assert s.find(100) is True
