class Solution:
    def moveElements(self, arr: list[int]) -> int:
        next_non_duplicate = 1
        i = 0

        while i < len(arr):
            if arr[next_non_duplicate - 1] != arr[i]:
                arr[next_non_duplicate] = arr[i]
                next_non_duplicate += 1

            i += 1

        return len(arr[:next_non_duplicate])
