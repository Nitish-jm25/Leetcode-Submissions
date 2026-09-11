class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=set()
        for a,b,c in permutations(digits,3):
            if a!=0 and c%2==0:
                n.add((a,b,c))
        return len(n)