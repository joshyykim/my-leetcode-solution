class Solution:
    def frequencySort(self, s: str) -> str:
        Cnt = sorted(collections.Counter(s).items(), key=lambda x:-x[1])
        return "".join([l[0]*l[1] for l in Cnt])