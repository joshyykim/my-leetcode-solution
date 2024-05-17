class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub, res = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i] + sub:
                sub = nums[i]
            else:
                sub = nums[i] + sub
            res = max(res, sub)
        return res