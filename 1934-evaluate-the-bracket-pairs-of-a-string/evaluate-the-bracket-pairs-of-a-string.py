class Solution(object):
    def evaluate(self, s, knowledge):
        key_map = dict(knowledge)
        res,i = [],0

        while i<len(s):
            if s[i]=="(":
                j=s.find(")",i+1)
                res.append(key_map.get(s[i+1:j],"?"))
                i=j
            else:
                res.append(s[i])
            i+=1
        return "".join(res)