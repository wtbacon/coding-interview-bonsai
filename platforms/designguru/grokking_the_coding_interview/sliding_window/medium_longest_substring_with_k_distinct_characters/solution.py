from collections import defaultdict


class Solution:
    def findLength(self, str1: str, k: int):
        max_length = 0
        left = 0
        char_freq: defaultdict[str, int] = defaultdict(int)

        for right in range(len(str1)):
            char_freq[str1[right]] += 1
            if len(char_freq.keys()) <= k:
                max_length = max(max_length, right - left + 1)
            else:
                char_freq[str1[left]] -= 1
                if char_freq[str1[left]] < 1:
                    char_freq.pop(str1[left])
                left += 1

        return max_length
