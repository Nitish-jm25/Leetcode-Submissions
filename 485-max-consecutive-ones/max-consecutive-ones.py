class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxi=0
        for num in nums:
            if num==1:
                cnt+=1
                maxi=max(cnt,maxi)
            else:
                cnt=0
        return maxi
