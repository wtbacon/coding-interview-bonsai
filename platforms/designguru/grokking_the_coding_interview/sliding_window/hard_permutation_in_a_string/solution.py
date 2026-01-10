from collections import defaultdict


class Solution:
    def findPermutation(self, str1: str, pattern: str):
        char_freq_in_ptn = defaultdict(int)
        for c in pattern:
            char_freq_in_ptn[c] += 1

        # `matched` explains that the number of distinct characters whose frequency requirement is fully satisfied.
        # Because the window size is fixed, if all character counts match => it must be a permutation.
        left, matched = 0, 0
        for right in range(len(str1)):
            right_char = str1[right]
            if right_char in char_freq_in_ptn:
                char_freq_in_ptn[right_char] -= 1
                if char_freq_in_ptn[right_char] == 0:
                    matched += 1

            if len(char_freq_in_ptn) == matched:
                return True

            if right >= len(pattern) - 1:
                left_char = str1[left]
                if left_char in char_freq_in_ptn:
                    if char_freq_in_ptn[left_char] == 0:
                        matched -= 1
                    # Need to increment after check whether the 'left_char' frequency is 0
                    # because you can't know whether it matched when the pattern contains duplicated characters.
                    char_freq_in_ptn[left_char] += 1
                left += 1

        return False
