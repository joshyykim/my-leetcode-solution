class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        d1, d2 = {}, {}
        for c in string.ascii_lowercase:
            d1[c], d2[c] = 0, 0
        for c in s1:
            d1[c] += 1
        for i in range(len(s1)):
            d2[s2[i]] += 1
        for i in range(len(s1), len(s2)+1):
            if d1 == d2: return True
            if i == len(s2): break
            d2[s2[i-len(s1)]] -= 1
            d2[s2[i]] += 1
        return False