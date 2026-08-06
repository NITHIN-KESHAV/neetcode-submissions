class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        db = {}

        for n in nums:
            if n in db:
                return True
            else:
                db[n] = True
        
        return False


