class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            if target - i in d:
                return [d[target-i], idx]
            else:
                d[i] = idx