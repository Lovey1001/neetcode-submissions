class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = reset = 0

        for i in nums:
            if i:
                count += 1
            else:
                count = 0
            reset = max(count, reset)
        return reset