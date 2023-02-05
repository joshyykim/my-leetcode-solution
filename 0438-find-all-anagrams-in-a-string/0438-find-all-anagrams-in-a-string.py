class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p): return []
        d1, d2 = {}, {}
        res = []
        for c in string.ascii_lowercase:
            d1[c], d2[c] = 0, 0
        for c in p:
            d1[c] += 1
        for i in range(len(p)):
            d2[s[i]] += 1
        for i in range(len(p),len(s)+1):
            if d1 == d2:
                res.append(i-len(p))
            if i==len(s): break
            d2[s[i-len(p)]] -= 1
            d2[s[i]] += 1
        return res