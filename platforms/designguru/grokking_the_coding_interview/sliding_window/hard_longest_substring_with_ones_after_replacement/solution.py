from collections import defaultdict


class Solution:
    def findLength(self, arr: list[int], k: int):
        max_length = 0
        left = 0
        binary_freq = defaultdict(int)

        for right in range(len(arr)):
            binary_freq[arr[right]] += 1

            while binary_freq[0] > k:
                binary_freq[arr[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
