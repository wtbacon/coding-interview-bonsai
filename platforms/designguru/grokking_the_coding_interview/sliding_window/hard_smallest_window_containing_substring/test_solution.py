from .solution import Solution


def test1():
    s = Solution()
    assert s.findSubstring("aabdec", "abc") == "abdec"


def test2():
    s = Solution()
    assert s.findSubstring("aabdec", "abac") == "aabdec"


def test3():
    s = Solution()
    assert s.findSubstring("abdbca", "abc") == "bca"


def test4():
    s = Solution()
    assert s.findSubstring("adcad", "abc") == ""


def test5():
    s = Solution()
    assert s.findSubstring("adadcmlwabc", "abc") == "abc"
