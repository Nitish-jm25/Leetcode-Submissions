class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq=Counter(nums)
        for n in nums:
            if freq[n]==1:
                return n