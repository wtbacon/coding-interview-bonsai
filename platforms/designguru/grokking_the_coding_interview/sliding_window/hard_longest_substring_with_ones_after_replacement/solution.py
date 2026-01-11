from collections import defaultdict


class Solution:
    def findLength(self, arr: list[int], k: int):
        max_length = 0
        window_start = 0
        binary_freq = defaultdict(int)

        for window_end in range(len(arr)):
            binary_freq[arr[window_end]] += 1

            while binary_freq[0] > k:
                binary_freq[arr[window_start]] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length
