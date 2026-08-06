class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        tmp = []

        for n in nums:
            if n != val:
                tmp.append(n)
        nums[:0] = tmp
        return len(tmp)

        

        