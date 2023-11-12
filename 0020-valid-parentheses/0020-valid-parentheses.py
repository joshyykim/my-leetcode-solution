class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for p in s:
            if p == "{" or p == "(" or p == "[":
                stack.append(p)
            else:
                try:
                    open_p = stack.pop()
                    if open_p + p != "()" and open_p + p != "[]" and open_p + p != "{}":
                        return False
                except:
                    return False
        return len(stack) == 0