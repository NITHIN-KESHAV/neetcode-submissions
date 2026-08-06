class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        b = len(nums) + 1

        bucket = [[] for _ in range(b)]

        result = []

        for n in nums:
            freq[n] += 1
        
        for x, cnt in freq.items():
                bucket[cnt].append(x)


        for cnt in range(len(bucket) -1, 0, -1):
            for x in bucket[cnt]:
                result.append(x)

                if len(result) == k:
                    return result

        






        