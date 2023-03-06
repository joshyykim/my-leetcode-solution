class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        li = [0 for _ in range(2001)]
        for n in arr:
            li[n] = 1
        res = 0
        for idx,i in enumerate(li):
            if i == 0:
                res += 1
            if res == k+1:
                return idx
        return res+1