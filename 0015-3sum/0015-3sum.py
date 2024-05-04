class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = set()
        m = 1
        
        while m < len(nums)-1:
            l, r = 0, len(nums)-1
            while l < m and m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    res.add((nums[l], nums[m], nums[r]))
                    l += 1
                elif nums[l] + nums[m] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            m += 1
        return res