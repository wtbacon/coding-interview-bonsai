class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2
        mid = 0
        num = 0

        while left <= right:
            mid = (right + left) // 2
            num = mid * mid
            if x == num:
                return mid
            elif num < x:
                left = mid + 1
            elif num > x:
                right = mid - 1 

        return right
