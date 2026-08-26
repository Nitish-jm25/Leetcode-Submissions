class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        cnt={}
        for c in magazine:
            cnt[c]=cnt.get(c,0)+1
        
        for ch in ransomNote:
            if ch not in cnt or cnt[ch]<=0:
                return False
            cnt[ch]-=1
        return True 