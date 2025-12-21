class Solution:
    def searchTriplets(self, arr: list[int]):
        triplets: list[list[int]] = []

        arr.sort()

        for i in range(len(arr)):
            if i > 0 and arr[i - 1] == arr[i]:
                continue
            self.search_pair(arr, triplets, -arr[i], i + 1)

        return triplets

    def search_pair(self, arr, triplets, target, left):
        right = len(arr) - 1

        while left < right:
            pair_sum = arr[left] + arr[right]
            if pair_sum == target:
                triplets.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left - 1] == arr[left]:
                    left += 1
                while left < right and arr[right + 1] == arr[right]:
                    right -= 1
            elif pair_sum > target:
                right -= 1
            elif pair_sum < target:
                left += 1
