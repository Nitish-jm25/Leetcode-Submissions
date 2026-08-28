class Solution(object):
    def moveZeroes(self, nums):
        k=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
        return nums