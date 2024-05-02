class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            strs[i] = (strs[i], "".join(sorted(strs[i])))
        
        d = {}
        for s, sortedS in strs:
            if sortedS in d:
                d[sortedS].append(s)
            else:
                d[sortedS] = [s]

        return list(d.values())