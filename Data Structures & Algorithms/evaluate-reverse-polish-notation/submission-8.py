class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        res = []

        for n in tokens:
            if n == '+':
                a = int(res.pop())
                b = int(res.pop())
                res.append(a+b)
            elif n == '-' :
                b = int(res.pop())
                a = int(res.pop())
                res.append(a-b)
            elif n == '*':
                res.append(int(res.pop()) * int(res.pop()))
            elif n == '/':
                b = int(res.pop())
                a = int(res.pop())
                res.append(int(a/b))
            else:
                res.append(int(n))
        return res[0]