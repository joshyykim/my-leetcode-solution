class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        alphabet = string.ascii_lowercase
        d = {_:set() for _ in alphabet}
        res = 0
        
        for idea in ideas:
            d[idea[:1]].add(idea[1:])
        
        for i in range(26):
            for j in range(26):
                if i != j:
                    redundant = len(d[alphabet[i]].intersection(d[alphabet[j]]))
                    res += (len(d[alphabet[i]])-redundant) * (len(d[alphabet[j]])-redundant)
        
        return res