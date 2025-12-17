from .solution import Solution


def test_1():
    s = Solution()
    assert s.search([1, 2, 3, 4, 6], 6) == [1, 3]


def test_2():
    s = Solution()
    assert s.search([2, 5, 9, 11], 11) == [0, 2]
