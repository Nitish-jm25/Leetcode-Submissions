class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        if s.count('1') < k:
            return ""
        
        left = 0
        ones_in_window = 0
        min_length = float("inf")
        best = ""

        for right in range(len(s)):
            if s[right] == "1":
                ones_in_window += 1
            while ones_in_window == k:
                current_string = s[left:right+1]
                current_length = len(current_string)

                if current_length < min_length:
                    min_length = current_length
                    best = current_string
                
                elif current_length == min_length:
                    best = min(best,current_string)
            
                if s[left] == "1":
                     ones_in_window -= 1
        
                left += 1
        return best