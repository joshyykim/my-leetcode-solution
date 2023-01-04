class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = [_ for _ in zip(*strs)]
        res = 0
        for c in cols:
            if list(c) != sorted(c):
                res += 1
        return res