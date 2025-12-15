class Solution:
    def numGoodPairs(self, nums: list[int]) -> int:
        pairCount = 0
        freq: dict[int, int] = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            pairCount += freq[num] - 1

        return pairCount
