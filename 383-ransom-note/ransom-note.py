class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
        return True