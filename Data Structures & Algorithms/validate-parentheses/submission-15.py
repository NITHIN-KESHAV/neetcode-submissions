class Solution:
    def isValid(self, s: str) -> bool:

        hm = {'}':'{', ']':'[', ')':'('}

        res = []

        for c in s:
            if c in hm:
                
                if not res or res[-1]!=hm[c]:
                    return False
                else:
                    res.pop()
            else:
                res.append(c)
        return res == []
                
        