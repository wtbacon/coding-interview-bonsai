from collections import defaultdict


class Solution:
    def findSubstring(self, str1: str, pattern: str):
        char_freq_in_ptn = defaultdict(int)
        for c in pattern:
            char_freq_in_ptn[c] += 1

        # `matched` explains that the total number of pattern characters that have been satisfied (including duplicates).
        # `matched` is a coverage counter, not just a completeness flag.
        # Why this works
        # - You must ensure every required occurrence is included.
        # - Duplicates matter ("AABC" ≠ "ABC").
        # - Shrinking the window must not break validity.
        left, matched, substring_start = 0, 0, 0
        min_length = len(str1) + 1
        for right in range(len(str1)):
            r_char = str1[right]
            if r_char in char_freq_in_ptn:
                char_freq_in_ptn[r_char] -= 1
                if char_freq_in_ptn[r_char] >= 0:
                    matched += 1

            while matched == len(pattern):
                if min_length > right - left + 1:
                    min_length = right - left + 1
                    substring_start = left

                l_char = str1[left]
                left += 1
                if l_char in char_freq_in_ptn:
                    if char_freq_in_ptn[l_char] == 0:
                        matched -= 1
                    char_freq_in_ptn[l_char] += 1

        return (
            "" if min_length > len(str1) else str1[substring_start : substring_start + min_length]
        )
