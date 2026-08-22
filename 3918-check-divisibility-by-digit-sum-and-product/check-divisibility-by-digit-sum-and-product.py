class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        sum_n = 0
        prod_n = 1
        while temp > 0:
            digit = temp % 10
            sum_n += digit
            prod_n *= digit
            temp //= 10
        divisor = sum_n + prod_n
        
        if divisor == 0:
            return False
        return n%divisor == 0