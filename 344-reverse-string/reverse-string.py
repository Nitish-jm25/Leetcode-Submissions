class Solution(object):
    def reverseString(self, s):
        j = len(s)-1
        i = 0
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1