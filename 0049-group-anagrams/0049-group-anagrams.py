class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedList = []
        for s in strs:
            sortedList.append((s, "".join(sorted(s))))
        
        d = {}
        for s, sortedS in sortedList:
            if sortedS in d:
                d[sortedS].append(s)
            else:
                d[sortedS] = [s]
        
        return list(d.values())