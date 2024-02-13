class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        cntList = []
        for i in d:
            cntList.append((i,d[i]))
        cntList.sort(key=lambda x:-x[1])
        
        return [cntList[i][0] for i in range(k)]