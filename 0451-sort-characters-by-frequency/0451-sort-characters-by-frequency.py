class Solution:
    def frequencySort(self, s: str) -> str:
        Cnt = sorted(collections.Counter(s).items(), key=lambda x:-x[1])
        return "".join([_[0]*_[1] for _ in Cnt])