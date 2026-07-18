class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes
        if x < 0:
            return False
        
        # Convert to string and compare with its reverse
        return str(x) == str(x)[::-1]