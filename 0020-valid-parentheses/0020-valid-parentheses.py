class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p == "{" or p == "(" or p == "[":
                stack.append(p)
            else:
                if not stack:
                    return False
                open_p = stack.pop()
                if open_p + p != "()" and open_p + p != "[]" and open_p + p != "{}":
                    return False
        return len(stack) == 0