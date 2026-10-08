class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        cnt = 0

        for c in s:
            if c=='(':
                if cnt>0:
                    ans.append(c)
                cnt+=1
            else:
                cnt-=1
                if cnt>0:
                    ans.append(c)
        return "".join(ans)