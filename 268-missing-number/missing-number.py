class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n+1):
            if i in nums:
                continue
            return i