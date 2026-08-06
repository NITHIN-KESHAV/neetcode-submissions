class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        cs = 0

        ls = 0

        for n in nums:
            cs = 1
            curr = n + 1
            while curr in nums:
                 cs += 1
                 curr += 1
            
            ls = max(ls,cs)
        
        return ls
            



        