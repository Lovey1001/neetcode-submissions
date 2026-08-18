class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        t = [0] * 2 * n
        left = 0
        right = len(nums) - 1
        for i in range(n-1, -1, -1):
            t[i] = nums[i]
            t[i + n] = nums[i]
        return t

        

        