class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sh, th = {}, {}

        if len(s) != len(t):
            return False
        
        for c in s:
            sh[c] = 1 + sh.get(c,0)
        
        for c in t:
            th[c] = 1 + th.get(c,0)

        
        if sh == th:
            return True

        else:
            return False     