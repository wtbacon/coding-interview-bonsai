from .solution import Solution


def test_1():
    s = Solution()
    assert (
        s.shortestDistance(
            ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], "fox", "dog"
        )
        == 5
    )


def test_2():
    s = Solution()
    assert s.shortestDistance(["a", "c", "d", "b", "a"], "a", "b") == 1


def test_3():
    s = Solution()
    assert s.shortestDistance(["a", "b", "c", "d", "e"], "a", "e") == 4
