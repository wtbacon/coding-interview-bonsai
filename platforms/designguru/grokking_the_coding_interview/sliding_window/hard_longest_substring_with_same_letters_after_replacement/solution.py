from collections import defaultdict


class Solution:
    def findLength(self, str1: str, k: int):
        max_length = 0
        window_start = 0
        max_repeat_char_count = 0
        char_freq = defaultdict(int)

        for window_end in range(len(str1)):
            char_freq[str1[window_end]] += 1

            # We only need to watch the frequency of `str1[window_end]`
            max_repeat_char_count = max(max_repeat_char_count, char_freq[str1[window_end]])

            # We can have a window which has one letter repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
            # If the remaining letters are more than 'k', it is the time to shrink the window as we are not allowed to replace more than 'k' letters
            while window_end - window_start + 1 - max_repeat_char_count > k:
                char_freq[str1[window_start]] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length
