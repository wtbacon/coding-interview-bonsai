from collections import defaultdict


class Solution:
    def findLength(self, fruits: list[str]):
        max_length = 0
        fruit_freq = defaultdict(int)
        sum_fruits = 0
        left = 0

        for right in range(len(fruits)):
            fruit_freq[fruits[right]] += 1
            sum_fruits += 1

            while len(fruit_freq) > 2:
                fruit_freq[fruits[left]] -= 1
                if fruit_freq[fruits[left]] == 0:
                    fruit_freq.pop(fruits[left])
                left += 1
                sum_fruits -= 1

            max_length = max(max_length, sum_fruits)

        return max_length
