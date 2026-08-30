class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        
        mini=min(nums)
        maxi=max(nums)

        mini_idx=nums.index(mini)
        maxi_idx=nums.index(maxi)

        i=min(mini_idx,maxi_idx)
        j=max(mini_idx,maxi_idx)

        del_front=j+1

        del_back=n-i

        del_mid=(i+1)+(n-j)

        return min(del_front,del_mid,del_back)