class Solution(object):
    def moveZeroes(self, nums):
        k=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
        return nums