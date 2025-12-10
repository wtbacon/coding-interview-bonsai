from .solution import Solution


def test_1():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal, Panama!")


def test_2():
    s = Solution()
    assert s.isPalindrome("Was it a car or a cat I saw?")
