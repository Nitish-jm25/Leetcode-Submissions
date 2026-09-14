class Solution(object):
    def generateParenthesis(self, n):
        result=[]

        def backtracking(cur_str,open_cnt,close_cnt):
            if len(cur_str)==2*n:
                result.append(cur_str)
                return
            if open_cnt<n:
                backtracking(cur_str+"(",open_cnt+1,close_cnt)
            if close_cnt<open_cnt:
                backtracking(cur_str+")",open_cnt,close_cnt+1)
        backtracking("",0,0)
        return result