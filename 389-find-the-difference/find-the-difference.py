class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tsort = sorted(t)
        ssort = sorted(s)

        i=0
        while i < len(ssort) and ssort[i]==tsort[i]:
            i+=1
        return tsort[i]