class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        res = 0
        
        for i in range(len(piles) //3 * 2):
            if i % 2 == 1:
                res += piles[i]
        return res