import math
class Solution(object):
    def smallestNumber(self, n, t):
        def product(n):
            p=1
            while n:
                p*=n%10
                n//=10
            return p

        while product(n) % t != 0:
            n+=1
        return n