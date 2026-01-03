import math


class Solution:
    def findMinSubArray(self, s: int, arr: list[int]):
        left = 0
        smallest_length = math.inf
        window_sum = 0

        for right in range(len(arr)):
            window_sum += arr[right]
            if window_sum >= s:
                smallest_length = min(smallest_length, right - left + 1)

            while window_sum >= s and left < right:
                window_sum -= arr[left]
                left += 1
                if window_sum >= s:
                    smallest_length = min(smallest_length, right - left + 1)

        return smallest_length if smallest_length != math.inf else 0
