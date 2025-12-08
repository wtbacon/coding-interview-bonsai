from .solution import Solution


def test_1():
    s = Solution()
    assert s.reverseVowels("hello") == "holle"


def test_2():
    s = Solution()
    assert s.reverseVowels("AEIOU") == "UOIEA"


def test_3():
    s = Solution()
    assert s.reverseVowels("DesignGUrus") == "DusUgnGires"
