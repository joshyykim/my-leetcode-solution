class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, li = [], [["(", 1, 0]]
        parentheses = ["(", ")"]
        
        while len(li[0][0]) < n*2:
            i = 0
            length = len(li)
            while i < length:
                string, num_opened, num_closed = li.pop(0)
                if num_opened < n:
                    li.append([string+"(", num_opened+1, num_closed])
                if num_opened > num_closed:
                    li.append([string+")", num_opened, num_closed+1])
                i += 1
                    
        for l in li:
            res.append(l[0])
        
        return res