from .solution import Solution


def test_1():
    s = Solution()
    assert s.mySqrt(8) == 2


def test_2():
    s = Solution()
    assert s.mySqrt(4) == 2


def test_3():
    s = Solution()
    assert s.mySqrt(8) == 2


def test_4():
    s = Solution()
    assert s.mySqrt(27) == 5


def test_5():
    s = Solution()
    assert s.mySqrt(9999) == 99
