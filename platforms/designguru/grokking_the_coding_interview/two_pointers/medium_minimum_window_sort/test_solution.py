from .solution import Solution


def test1():
    s = Solution()
    assert s.sort([1, 2, 5, 3, 7, 10, 9, 12]) == 5


def test2():
    s = Solution()
    assert s.sort([1, 3, 2, 0, -1, 7, 10]) == 5


def test3():
    s = Solution()
    assert s.sort([1, 2, 3]) == 0


def test4():
    s = Solution()
    assert s.sort([3, 2, 1]) == 3


def test5():
    s = Solution()
    assert s.sort([3, 3, 2, 2]) == 4


def test6():
    s = Solution()
    assert s.sort([56, 67, 5, 31, 64]) == 5


def test7():
    s = Solution()
    assert s.sort([2, 3, 3, 2]) == 3
