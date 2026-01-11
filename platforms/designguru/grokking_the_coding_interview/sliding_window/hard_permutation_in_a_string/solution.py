from collections import defaultdict


class Solution:
    def findPermutation(self, str1: str, pattern: str):
        char_freq_in_ptn = defaultdict(int)
        for c in pattern:
            char_freq_in_ptn[c] += 1

        # `matched` explains that the number of distinct characters whose frequency requirement is fully satisfied.
        # Because the window size is fixed, if all character counts match => it must be a permutation.
        window_start, matched = 0, 0
        for window_end in range(len(str1)):
            window_end_char = str1[window_end]
            if window_end_char in char_freq_in_ptn:
                char_freq_in_ptn[window_end_char] -= 1
                if char_freq_in_ptn[window_end_char] == 0:
                    matched += 1

            if len(char_freq_in_ptn) == matched:
                return True

            if window_end >= len(pattern) - 1:
                window_start_char = str1[window_start]
                if window_start_char in char_freq_in_ptn:
                    if char_freq_in_ptn[window_start_char] == 0:
                        matched -= 1
                    # Need to increment after check whether the 'window_start_char' frequency is 0
                    # because you can't know whether it matched when the pattern contains duplicated characters.
                    char_freq_in_ptn[window_start_char] += 1
                window_start += 1

        return False
