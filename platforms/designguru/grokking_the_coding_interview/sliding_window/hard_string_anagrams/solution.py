from collections import defaultdict


class Solution:
    def findStringAnagrams(self, str1: str, pattern: str):
        result_indices = []
        char_freq_in_ptn = defaultdict(int)

        for c in pattern:
            char_freq_in_ptn[c] += 1

        # `matched` explains that the number of distinct characters whose frequency requirement is fully satisfied.
        # Because the window size is fixed, if all character counts match => it must be an anagram.
        window_start, matched = 0, 0
        for window_end in range(len(str1)):
            char_window_end = str1[window_end]

            if char_window_end in char_freq_in_ptn:
                char_freq_in_ptn[char_window_end] -= 1
                if char_freq_in_ptn[char_window_end] == 0:
                    matched += 1

            if matched == len(char_freq_in_ptn):
                result_indices.append(window_start)

            if window_end >= len(pattern) - 1:
                char_window_start = str1[window_start]
                window_start += 1
                if char_window_start in char_freq_in_ptn:
                    if char_freq_in_ptn[char_window_start] == 0:
                        matched -= 1
                    char_freq_in_ptn[char_window_start] += 1

        return result_indices
