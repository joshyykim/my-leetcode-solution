class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        Cnt = sorted(collections.Counter(s).items(), key=lambda x:-x[1])
        for c,cnt in Cnt:
            ans += c * cnt
        return ans