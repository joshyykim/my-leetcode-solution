class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        return sum([piles[i] for i in range(len(piles) //3 * 2) if i % 2 == 1])