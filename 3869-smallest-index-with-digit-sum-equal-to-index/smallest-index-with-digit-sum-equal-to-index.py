class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for i in range(len(nums)):
            s=str(nums[i])
            sum=0
            mini=float("inf")
            for n in s:
                sum+=int(n)
            if sum==i:
                return min(mini,i)
        return -1