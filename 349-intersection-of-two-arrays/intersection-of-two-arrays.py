class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        res=set()
        ss=set(nums1)
        for num in nums2:
            if num in ss:
                res.add(num)
        return list(res)