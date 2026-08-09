class Solution(object):
    def findMissingElements(self, nums):
        if not nums :
            return []
        mini = min(nums)
        maxi = max(nums)
        num_set = set(nums)

        return [i for i in range(mini,maxi+1) if i not in num_set]
        