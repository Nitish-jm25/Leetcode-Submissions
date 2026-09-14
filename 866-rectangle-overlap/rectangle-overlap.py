class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        ovr_width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        ovr_height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        
        return ovr_width > 0 and ovr_height > 0
