from .solution import Solution


def test1():
    s = Solution()
    assert s.findPermutation("oidbcaf", "abc") is True


def test2():
    s = Solution()
    assert s.findPermutation("odicf", "dc") is False


def test3():
    s = Solution()
    assert s.findPermutation("bcdxabcdy", "bcdyabcdx") is True


def test4():
    s = Solution()
    assert s.findPermutation("aaacb", "abc") is True


def test5():
    s = Solution()
    assert s.findPermutation("testcase", "acest") is True
