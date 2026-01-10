from .solution import Solution


def test1():
    s = Solution()
    assert s.findStringAnagrams("ppqp", "pq") == [1, 2]


def test2():
    s = Solution()
    assert s.findStringAnagrams("abbcabc", "abc") == [2, 3, 4]


def test3():
    s = Solution()
    assert s.findStringAnagrams("testest", "est") == [0, 1, 2, 3, 4]
