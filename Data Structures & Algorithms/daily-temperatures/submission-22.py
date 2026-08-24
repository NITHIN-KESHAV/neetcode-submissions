class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)

        s = []

        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                prev_index = s.pop()
                res[prev_index] = i - prev_index
            s.append(i)
        return res