class Solution:
    def characterReplacement(self, s: str, k: int) -> int:             
        d = {}
        
        for c in string.ascii_uppercase:
            d[c] = 0
        for i in range(k):
            d[s[i]] += 1
            
        res = sum(d.values())

        for i in range(k,len(s)):
            d[s[i]] += 1
            num_replace = sum(d.values()) - max(d.values())
            if num_replace <= k:
                if sum(d.values()) > res:
                    res = sum(d.values())
            else:
                d[s[i-sum(d.values())+1]] -= 1
        return res