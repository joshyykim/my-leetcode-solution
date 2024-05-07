class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, mid, r = 0, len(nums) // 2, len(nums)-1
        
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums)-1
        if nums[l] > target or nums[r] < target:
            return -1
        
        while l < mid and mid < r:
            if nums[mid] > target:
                r = mid
                mid = (l + r) // 2
            elif nums[mid] < target:
                l = mid
                mid = (l + r) // 2
            else:
                return mid
        return -1