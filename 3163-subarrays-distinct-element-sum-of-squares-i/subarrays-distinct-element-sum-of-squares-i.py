class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        for begin in range(n):
            for end in range(begin,n):
                total+=len(set(nums[begin:end+1]))**2
        return total