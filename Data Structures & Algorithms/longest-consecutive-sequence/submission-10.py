class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ns = set(nums)
        
        ls = 0

        for n in ns:
            if n-1 not in ns:
                cs  = 1
                while (n + cs) in ns:
                    cs +=1
            
                ls = max(ls, cs)
        return ls



        