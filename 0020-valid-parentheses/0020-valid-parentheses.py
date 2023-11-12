class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"{": "}", "(": ")", "[": "]"}
        for p in s:
            if p in d:
                stack.append(p)
            else:
                if stack and p == d[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0