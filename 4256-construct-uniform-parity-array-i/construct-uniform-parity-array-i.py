class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2 = [0] * len(nums1) 
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if j!=i:
                    nums2[i]=nums1[i]-nums1[j]
                nums2[i]=nums1[i]
        return True