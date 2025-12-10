from .solution import Solution


def test_1():
    s = Solution()
    assert s.isAnagram("listen", "silent") is True


def test_2():
    s = Solution()
    assert s.isAnagram("rat", "car") is False


def test_3():
    s = Solution()
    assert s.isAnagram("hello", "world") is False
