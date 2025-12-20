class Solution:
    def makeSquares(self, arr: list[int]):
        low, high = 0, len(arr) - 1
        next_highest_idx = len(arr) - 1
        ans = [0 for _ in range(len(arr))]

        while low <= high:
            if abs(arr[low]) < abs(arr[high]):
                ans[next_highest_idx] = arr[high] ** 2
                high -= 1
                next_highest_idx -= 1
            else:
                ans[next_highest_idx] = arr[low] ** 2
                low += 1
                next_highest_idx -= 1

        return ans
