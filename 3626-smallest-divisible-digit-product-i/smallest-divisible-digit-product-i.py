class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True :
            digit = math.prod(int(d) for d in str(n))
            if digit % t == 0:
                return n
            n += 1