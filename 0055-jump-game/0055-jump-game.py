class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        left, right = 0, nums[0]
        
        while left < right:
            left += 1
            if right < left + nums[left]:
                right = left + nums[left]
            
            if right >= len(nums)-1:
                return True
        return False