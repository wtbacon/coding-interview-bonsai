from .solution import Solution


def test1():
    s = Solution()
    assert s.searchTriplets([-3, 0, 1, 2, -1, 1, -2]) == [
        [-3, 1, 2],
        [-2, 0, 2],
        [-2, 1, 1],
        [-1, 0, 1],
    ]


def test2():
    s = Solution()
    assert s.searchTriplets([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]]
