class Solution(object):
    def findTheDifference(self, s, t):
        sum = 0
        for c in s:
            sum -= ord(c)
        for c in t:
            sum += ord(c)
        return chr(sum)