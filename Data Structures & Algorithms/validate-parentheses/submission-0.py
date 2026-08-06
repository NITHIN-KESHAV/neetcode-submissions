class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c2O = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in c2O:
                if stack and stack[-1] == c2O[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False