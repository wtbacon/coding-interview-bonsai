from collections import defaultdict


class Solution:
    def findPermutation(self, str1: str, pattern: str):
        char_freq_in_ptn = defaultdict(int)
        for r in pattern:
            char_freq_in_ptn[r] += 1

        left = 0
        for right in range(len(str1)):
            r = str1[right]
            while left < right and r not in char_freq_in_ptn:
                l = str1[left]
                if l in pattern:
                    char_freq_in_ptn[l] += 1
                left += 1
            if r in char_freq_in_ptn:
                char_freq_in_ptn[r] -= 1
                if char_freq_in_ptn[r] == 0:
                    del char_freq_in_ptn[r]
                if len(char_freq_in_ptn) == 0:
                    return True

        return False
