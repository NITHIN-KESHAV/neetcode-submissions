class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        db = set()

        for n in nums:
            db.add(n) 
        
        if len(nums) > len(db):
            return True
        
        else:
            return False


