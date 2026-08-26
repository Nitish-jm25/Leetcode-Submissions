class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen=float("inf")
        left=0
        currentSum=0
        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                minlen = min(minlen,right-left+1)
                currentSum -= nums[left]
                left += 1
        return minlen if minlen != float("inf") else 0