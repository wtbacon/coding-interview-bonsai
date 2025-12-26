class Solution:
    def sort(self, arr):
        i = 0
        next_0_idx, next_2_idx = 0, len(arr) - 1

        while i <= next_2_idx:
            if arr[i] == 0:
                arr[next_0_idx], arr[i] = arr[i], arr[next_0_idx]
                next_0_idx += 1
                i += 1  # The value at the swapped next_0_idx has already been processed and is guaranteed to be either 0(when i == next_0_idx) or 1.
            elif arr[i] == 2:
                arr[next_2_idx], arr[i] = arr[i], arr[next_2_idx]
                next_2_idx -= 1
                # The value at the swapped next_2_idx has not been processed yet and i is not incremented.
            else:
                i += 1

        return arr
