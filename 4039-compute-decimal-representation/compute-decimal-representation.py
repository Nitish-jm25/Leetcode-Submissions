class Solution(object):
    def decimalRepresentation(self, n):
        num = str(n)
        length=len(num)
        result = []
        places="1"+("0"*(length-1))
        for i in range(length):
            digit = num[i]
            digit = int(digit)*int(places)
            result.append(int(digit))
            places=str(int(places)//10)
        result=[n for n in result if n>0]
        return result