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
        


        # l = 0
        # for num in nums:
        #     if l < 2 or num != nums[l - 2]:
        #         nums[l] = num
        #         l += 1
        # return l


        # n = len(nums)

        # if n <= 2:
        #     return n

        # count = Counter(nums)
        # i = 0   

        # for n in count:
        #     nums[i] = n
        #     count[n] -= 1
        #     i += 1

        #     if count[n] >= 1:
        #         nums[i] = 1
        #         count[n] -= 1
        #         i += 1

        # return i







        n = len(nums)
        if n <= 2:
            return n

        count = Counter(nums)
        i = 0
        for num in count:
            nums[i] = num
            count[num] -= 1
            i += 1
            if count[num] >= 1:
                nums[i] = num
                count[num] -= 1
                i += 1
        return i



        