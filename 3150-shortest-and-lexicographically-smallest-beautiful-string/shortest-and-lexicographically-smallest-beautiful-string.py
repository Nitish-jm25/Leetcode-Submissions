class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1")<k:
            return ""
        left,ones,best=0,0,""
        minlen=float("inf")

        for right in range(len(s)):
            if s[right]=="1":
                ones+=1
            while ones==k:
                curr_str=s[left:right+1]
                if len(curr_str)<minlen or (curr_str<best and len(curr_str)==minlen):
                    best = curr_str
                    minlen=len(curr_str)
                if s[left]=="1":
                    ones-=1
                left+=1
        return best