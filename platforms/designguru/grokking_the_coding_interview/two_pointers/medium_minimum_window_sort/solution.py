import math


class Solution:
    def sort(self, arr):
        low, high = 0, len(arr) - 1
        while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
            low += 1
        while high > -1 and arr[high - 1] <= arr[high]:
            high -= 1
        if low == len(arr) - 1:
            return 0

        sub_max = -math.inf
        sub_min = math.inf
        for i in range(low, high + 1):
            sub_max = max(sub_max, arr[i])
            sub_min = min(sub_min, arr[i])

        while 0 < low and arr[low - 1] > sub_min:
            low -= 1
        while high < len(arr) - 1 and arr[high + 1] < sub_max:
            high += 1

        return high - low + 1
