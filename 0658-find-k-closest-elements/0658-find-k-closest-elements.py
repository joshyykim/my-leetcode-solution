class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ### method 2 (heap)
        arr.sort(key=lambda i:abs(i-x))
        heap = []
        for i in range(k):
            heapq.heappush(heap, arr[i])
        return sorted(heap)