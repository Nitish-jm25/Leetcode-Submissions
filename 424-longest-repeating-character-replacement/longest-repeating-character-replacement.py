class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        max_count=0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            max_count=max(max_count,freq[s[right]])
            current_length=right-left+1
            if current_length-max_count>k:
                freq[s[left]]-=1
                left+=1
        return len(s)-left