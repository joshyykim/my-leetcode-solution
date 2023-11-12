class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_mapped = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        res = []
        
        def helper(string, digits):
            if digits == "":
                if string != "":
                    res.append(string)
                return
            
            for letter in digits_mapped[int(digits[0])]:
                helper(string+letter, digits[1:])
        helper("", digits)    
        return res