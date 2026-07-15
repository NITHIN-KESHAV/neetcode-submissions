class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        if len(s) == len(t):
            for c in s:
                dicts[c] = dicts.get(c,0)+1
            
            for c in t:
                dictt[c] = dictt.get(c,0)+1
            
            if dicts == dictt:
                return True
        return False
            

