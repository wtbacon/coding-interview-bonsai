class Solution:
    def find(self, num: int) -> bool:
        slow, fast = num, num

        while True:
            slow = self._calculate(slow)
            fast = self._calculate(self._calculate(fast))
            if slow == fast:
                break

        return slow == 1

    def _calculate(self, num: int) -> int:
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit**2
            num = num // 10
        return _sum
