class Solution(object):
    def reverseDegree(self, s):
        return sum((i+1)*(26-(ord(c)-ord('a'))) for i,c in enumerate(s))