from collections import defaultdict


class Solution:
    def findLength(self, fruits: list[str]):
        max_length = 0
        fruit_freq = defaultdict(int)
        sum_fruits = 0
        window_start = 0

        for window_end in range(len(fruits)):
            fruit_freq[fruits[window_end]] += 1
            sum_fruits += 1

            while len(fruit_freq) > 2:
                fruit_freq[fruits[window_start]] -= 1
                if fruit_freq[fruits[window_start]] == 0:
                    fruit_freq.pop(fruits[window_start])
                window_start += 1
                sum_fruits -= 1

            max_length = max(max_length, sum_fruits)

        return max_length
