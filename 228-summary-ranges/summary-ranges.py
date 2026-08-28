class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l=[]
        i,n=0,len(nums)
        while i < n:
            start=i
            while i+1<n and nums[i+1]==nums[i]+1:
                i+=1
            if start==i:
                l.append(f"{nums[start]}")
            else:
                l.append(f"{nums[start]}->{nums[i]}")
            i+=1
        return l
                