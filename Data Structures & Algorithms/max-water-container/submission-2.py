class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # max_a = 0
        
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         mw = min(heights[i], heights[j]) * (j - i)
        #         max_a = max(max_a,mw)
        # return max_a


        l,r = 0, len(heights) - 1

        max_w = 0

        while l < r:
            a =  min(heights[l], heights[r]) * (r - l)
            max_w = max(max_w, a)

            if heights[l] < heights[r]:
                l += 1

            else:

                r -= 1

        return max_w