from .solution import Solution


def test1():
    s = Solution()
    assert s.findWordConcatenation("catfoxcat", ["cat", "fox"]) == [0, 3]


def test2():
    s = Solution()
    assert s.findWordConcatenation("catcatfoxfox", ["cat", "fox"]) == [3]
