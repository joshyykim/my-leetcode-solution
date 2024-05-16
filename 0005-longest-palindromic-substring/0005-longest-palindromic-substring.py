class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: return s
        
        self.res = ""
        def helper(i, j):
            while i < len(s) and i-j >= 0:
                if s[i] == s[i-j]:
                    if j+1 > len(self.res):
                        self.res = s[i-j:i+1]
                else:
                    break
                j += 2
                i += 1
            
        for i in range(len(s)):
            helper(i, 0)
            helper(i, 1)
            
        return self.res