class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(val1, val2, op):
            if op == "+":
                return val1 + val2
            elif op == "-":
                return val1 - val2
            elif op == "*":
                return val1 * val2
            else:
                return int(val1 / val2)
            
        stack = [int(tokens.pop(0))]
        
        while tokens:
            val = tokens.pop(0)
            if val.strip('-').isnumeric():
                stack.append(int(val))
            else:
                stack.append(calculate(stack.pop(-2), stack.pop(-1), val))
        return stack[0]
                    