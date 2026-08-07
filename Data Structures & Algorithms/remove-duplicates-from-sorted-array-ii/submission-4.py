class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # l, r = 0,0

        # while r < len(nums):
        #     count = 1
        #     while r + 1 < len(nums) and nums[r] == nums[r+1]:
        #         count += 1
        #         r += 1

        #     for i in range(min(2, count)):
        #         nums[l] = nums[r]
        #         l += 1
        #     r += 1
            
        # return l
        


        l = 0
        for num in nums:
            if l < 2 or num != nums[l - 2]:
                nums[l] = num
                l += 1
        return l











        