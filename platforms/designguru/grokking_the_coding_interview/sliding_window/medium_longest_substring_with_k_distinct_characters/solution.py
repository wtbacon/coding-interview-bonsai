from collections import defaultdict


class Solution:
    def findLength(self, str1: str, k: int):
        max_length = 0
        window_start = 0
        char_freq: defaultdict[str, int] = defaultdict(int)

        for window_end in range(len(str1)):
            char_freq[str1[window_end]] += 1
            if len(char_freq.keys()) <= k:
                max_length = max(max_length, window_end - window_start + 1)
            else:
                char_freq[str1[window_start]] -= 1
                if char_freq[str1[window_start]] < 1:
                    char_freq.pop(str1[window_start])
                window_start += 1

        return max_length
