class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = Counter(nums)
        for k in d:
            if d[k] > 1:
                return True
        return False