class Solution(object):
    def plusOne(self, digits):
        res=""
        l=[]
        for i in range(len(digits)):
            res+=str(digits[i])
        n=str(int(res)+1)
        for i in range(len(n)):
            l.append(int(n[i]))
        return l