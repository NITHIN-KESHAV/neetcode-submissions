class Solution:
    def calPoints(self, operations: List[str]) -> int:

        s = []

        for n in operations:
            if n == '+':
                a = s[-1]
                b = s[-2]
                s.append(a+b)
            elif n == 'C':
                s.pop()
            elif n == 'D':
                s.append(2 * s[-1])
            else:
                s.append(int(n))
        return sum(s)