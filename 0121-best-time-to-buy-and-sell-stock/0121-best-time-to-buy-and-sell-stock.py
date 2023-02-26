class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        begin, end = maxsize, 0
        for i in prices:
            if i <= begin:
                begin = i
                end = i
            if i >= end:
                end = i
            res.append(end-begin)
        return max(res)