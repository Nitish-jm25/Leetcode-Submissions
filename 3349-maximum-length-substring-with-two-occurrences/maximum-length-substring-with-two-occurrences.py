class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res=l=0
        fq=defaultdict(int)
        for r,c in enumerate(s):
            fq[c]+=1
            while fq[c]>2:
                fq[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res