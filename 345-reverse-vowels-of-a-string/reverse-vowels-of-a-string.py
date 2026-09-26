class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        vowels="aeoiuAEIOU"
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return "".join(s)