from .solution import Solution


def test1():
    s = Solution()
    assert s.compare(str1="xy#z", str2="xzz#")


def test2():
    s = Solution()
    assert not s.compare(str1="xy#z", str2="xyz#")


def test3():
    s = Solution()
    assert s.compare(str1="xp#", str2="xyz##")


def test4():
    s = Solution()
    assert s.compare(str1="xywrrmp", str2="xywrrmu#p")
