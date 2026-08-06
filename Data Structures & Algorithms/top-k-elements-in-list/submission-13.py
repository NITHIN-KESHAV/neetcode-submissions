class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        res = []

        b = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq[n] = 1 + freq.get(n,0)


        for n, c in freq.items():
            b[c].append(n)

        for i in range(len(b)-1,0,-1):
            for num in b[i]:

                res.append(num)
            if len(res) == k:
                return res
