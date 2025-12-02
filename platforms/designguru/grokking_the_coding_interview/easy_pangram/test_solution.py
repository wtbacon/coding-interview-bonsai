from .solution import Solution


def test_example():
    s = Solution()
    assert s.checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") is True
