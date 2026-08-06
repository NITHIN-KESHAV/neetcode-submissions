class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ls = 0
        

        for n in nums:
            cs = 1
            curr = n

            while curr + 1 in nums:
                cs+=1
                curr+= 1
            
            ls = max(ls, cs)
        
        return ls

            

        