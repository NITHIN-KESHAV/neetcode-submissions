class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1


        while l < r:
            if target == numbers[l] + numbers[r]:
                return [l+1,r+1]

            if r != l and numbers[l] + numbers[r] > target:
                r -= 1

            elif r != l and numbers[l] + numbers[r] < target:
                l += 1
            
            

       
        