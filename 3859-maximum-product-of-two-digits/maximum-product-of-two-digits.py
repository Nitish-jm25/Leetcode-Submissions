class Solution:
    def maxProduct(self, n: int) -> int:
        nums = str(n)
        max1 = 0
        max2 = 0
        for num in nums:
            val = int(num)
            if val > max1 :
                max2 = max1
                max1 = val
            elif val > max2:
                max2 = val
        return max1*max2

