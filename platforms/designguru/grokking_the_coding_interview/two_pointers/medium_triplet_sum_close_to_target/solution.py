import math


class Solution:
    _closest_diff = 20_000

    def searchTriplet(self, arr, target_sum):
        arr.sort()

        for i in range(len(arr)):
            self._search_diff(arr, i, i + 1, target_sum)

        return self._closest_diff + target_sum

    def _search_diff(self, arr, i, left, target_sum):
        right = len(arr) - 1
        while left < right:
            triplet_sum = arr[i] + arr[left] + arr[right]
            triplet_diff = triplet_sum - target_sum
            if abs(triplet_diff) < abs(self._closest_diff):
                self._closest_diff = triplet_diff
            elif abs(triplet_diff) == abs(self._closest_diff) and triplet_sum < target_sum:
                self._closest_diff = triplet_diff

            if triplet_sum > target_sum:
                right -= 1
            else:
                left += 1
