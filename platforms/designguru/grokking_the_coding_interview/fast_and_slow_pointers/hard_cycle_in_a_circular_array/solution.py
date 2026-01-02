class Solution:
    def loopExists(self, arr: list[int]):
        for i in range(len(arr)):
            slow, fast = i, i
            is_forwarding = arr[i] > 0

            while True:
                slow = self._next_index(arr, slow, is_forwarding)
                fast = self._next_index(arr, fast, is_forwarding)
                if fast != -1:
                    fast = self._next_index(arr, fast, is_forwarding)

                if slow == -1 or fast == -1:
                    break

                if slow == fast:
                    return True

        return False

    def _next_index(self, arr, i, is_forwarding):
        direction = arr[i] > 0
        if direction != is_forwarding:
            return -1

        next_index = (i + arr[i]) % len(arr)
        if i == next_index:
            return -1

        return next_index
