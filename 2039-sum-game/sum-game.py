class Solution:
    def sumGame(self, num: str) -> bool:
        leftsum,rightsum = 0,0
        rightq,leftq = 0,0
        for i in range(len(num)//2):
            if num[i]=="?":
                leftq += 1
            else:
                leftsum += int(num[i])
        for i in range(len(num)//2,len(num)):
            if num[i]=="?":
                rightq += 1
            else:
                rightsum += int(num[i])
        return (leftsum - rightsum)*2 != (rightq - leftq)*9