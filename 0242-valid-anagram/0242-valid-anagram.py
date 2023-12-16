class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        
        for c in cnt_s:
            if c not in cnt_t or cnt_s[c] != cnt_t[c]:
                return False
            
        for c in cnt_t:
            if c not in cnt_t or cnt_s[c] != cnt_t[c]:
                return False
        return True