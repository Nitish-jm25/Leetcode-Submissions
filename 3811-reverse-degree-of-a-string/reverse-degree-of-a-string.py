class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            rev_val = 123 - ord(s[i])
            sum += (i+1)*rev_val
        return sum