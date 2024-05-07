class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l < r:
            mid = (l + r) // 2
            hours_needed = sum([math.ceil(_/mid) for _ in piles])
            if hours_needed <= h:
                res = min(res, mid)
                r = mid
            else:
                l = mid + 1
        return res