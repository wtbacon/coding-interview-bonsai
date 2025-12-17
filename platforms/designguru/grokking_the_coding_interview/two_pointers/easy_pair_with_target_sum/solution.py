class Solution:
    def search(self, arr: list[int], target: int) -> list[int]:
        head, tail = 0, len(arr) - 1
        while head < tail:
            if arr[head] + arr[tail] == target:
                return [head, tail]
            elif arr[head] + arr[tail] > target:
                tail -= 1
            elif arr[head] + arr[tail] < target:
                head += 1

        return [-1, -1]

    # HashTable pattern
    def pair_with_target_sum(self, arr: list[int], target_sum: int) -> list[int]:
        nums = {}
        for i, num in enumerate(arr):
            if target_sum - num in nums:
                return [nums[target_sum - num], i]
            else:
                nums[num] = i

        return [-1, -1]
