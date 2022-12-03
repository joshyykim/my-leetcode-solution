class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        d1, d2 = {}, {}
        for c1 in word1:
            if c1 in d1: d1[c1] += 1
            else: d1[c1] = 1
        for c2 in word2:
            if c2 in d2: d2[c2] += 1
            else: d2[c2] = 1
        l1, l2 = [sorted(list(d1.keys())), sorted(list(d1.values()))], [sorted(list(d2.keys())), sorted(list(d2.values()))]
        return l1[0] == l2[0] and l1[1] == l2[1]