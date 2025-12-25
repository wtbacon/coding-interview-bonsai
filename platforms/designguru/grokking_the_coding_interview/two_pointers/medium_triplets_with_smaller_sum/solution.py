class Solution:
    def searchTriplets(self, arr, target):
        count = 0

        arr.sort()
        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
