class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        while len(stones) > 1:
            heapq.heappush(stones, (heapq._heappop_max(stones) - heapq._heappop_max(stones)))
            heapq._heapify_max(stones)
        
        return stones[0]