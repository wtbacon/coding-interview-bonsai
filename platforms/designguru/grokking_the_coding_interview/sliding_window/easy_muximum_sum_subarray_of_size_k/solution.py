class Solution:
    def findMaxSumSubArray(self, k: int, arr: list[int]):
        window_max, window_sum = 0, 0
        for i in range(len(arr)):
            window_sum += arr[i]

            if i >= k - 1:
                window_max = max(window_max, window_sum)
                window_sum -= arr[i - k + 1]

        return window_max
