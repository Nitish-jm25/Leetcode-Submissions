class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_score=float("inf")
        max_score=0
        suffix=[0]*n
        for i in range(n-1,-1,-1):
            min_score=min(min_score,nums[i])
            suffix[i]=min_score
        for i in range(n):
            max_score=max(max_score,nums[i])
            score=max_score-suffix[i]
            if score<=k:
                return i
        return -1