class Solution(object):
    def uniformArray(self, nums1):
        mn=float("inf")
        oddcnt=0
        for x in nums1:
            mn=min(mn,x)
            if x%2==1:
                oddcnt+=1
        return mn%2==1 or oddcnt==0