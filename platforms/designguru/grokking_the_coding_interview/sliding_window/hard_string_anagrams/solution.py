from collections import defaultdict


class Solution:
    def findStringAnagrams(self, str1: str, pattern: str):
        result_indices = []
        char_freq_in_ptn = defaultdict(int)

        for c in pattern:
            char_freq_in_ptn[c] += 1

        left, matched = 0, 0
        for right in range(len(str1)):
            char_right = str1[right]

            if char_right in char_freq_in_ptn:
                char_freq_in_ptn[char_right] -= 1
                if char_freq_in_ptn[char_right] == 0:
                    matched += 1

            if matched == len(char_freq_in_ptn):
                result_indices.append(left)

            if right >= len(pattern) - 1:
                char_left = str1[left]
                left += 1
                if char_left in char_freq_in_ptn:
                    if char_freq_in_ptn[char_left] == 0:
                        matched -= 1
                    char_freq_in_ptn[char_left] += 1

        return result_indices
