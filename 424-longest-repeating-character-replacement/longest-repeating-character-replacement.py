class Solution(object):
    def characterReplacement(self, s, k):
        left=0
        freq={}
        result=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq=max(freq.values())
            current_len=right-left+1
            if current_len-max_freq>k:
                freq[s[left]]-=1
                left+=1
            result=max(result,right-left+1)
        return result