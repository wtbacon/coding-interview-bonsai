from collections import defaultdict


class Solution:
    def findLength(self, str1: str, k: int):
        max_length = 0
        left = 0
        max_repeat_char_count = 0
        char_freq = defaultdict(int)

        for right in range(len(str1)):
            char_freq[str1[right]] += 1

            # We only need to watch the frequency of `str1[right]`
            max_repeat_char_count = max(max_repeat_char_count, char_freq[str1[right]])

            # We can have a window which has one letter repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # If the remaining letters are more than 'k', it is the time to shrink the window as we are not allowed to replace more than 'k' letters
            while right - left + 1 - max_repeat_char_count > k:
                char_freq[str1[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
