class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        reverse_cnt = [(cnt[k], k) for k in cnt]
        reverse_cnt.sort(key=lambda x: -x[0])
        return [reverse_cnt[i][1] for i in range(k)]