class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            if c in d: d[c] += 1
            else: d[c] = 1
        li = []
        for k in d.keys():
            li.append([k,d[k]])
        li.sort(key=lambda x:-x[1])
        return "".join([l[0]*l[1] for l in li])