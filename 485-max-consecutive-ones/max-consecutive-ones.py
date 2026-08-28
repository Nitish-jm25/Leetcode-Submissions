class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi,cnt = 0,0
        for num in nums:
            if num==0:
                cnt = 0
                continue
            cnt+=1
            maxi=max(maxi,cnt)
        return maxi
