class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        target, res = nums[-1], nums[-1]
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target or nums[l] < target:
                res = min(res, nums[mid], nums[l])
                r = mid
            else:
                l = mid + 1
        return res