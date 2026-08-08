class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     j = target - nums[i]
 
        #     if j in nums and nums.index(j) != i:
        #         return sorted([i, nums.index(j)])
            
        d = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            d[n] = i
