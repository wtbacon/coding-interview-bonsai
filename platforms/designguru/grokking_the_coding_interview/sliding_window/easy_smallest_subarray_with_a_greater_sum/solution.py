import math


class Solution:
    def findMinSubArray(self, s: int, arr: list[int]):
        window_start = 0
        smallest_length = math.inf
        window_sum = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_sum >= s:
                smallest_length = min(smallest_length, window_end - window_start + 1)

            while window_sum >= s and window_start < window_end:
                window_sum -= arr[window_start]
                window_start += 1
                if window_sum >= s:
                    smallest_length = min(smallest_length, window_end - window_start + 1)

        return smallest_length if smallest_length != math.inf else 0
