class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            new_stone = stones.pop(-1) - stones.pop(-1)
            if new_stone != 0:
                stones.insert(bisect.bisect(stones, new_stone), new_stone)

        if len(stones) > 0:
            return stones[0]
        else:
            return 0