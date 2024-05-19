class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = nums[0]
        
        for i in range(len(nums)-1):
            if i > end:
                return False
            if nums[i] + i > end:
                end = i + nums[i]
                
        return end >= len(nums)-1
        
#         if len(nums) == 1:
#             return True
#         left, right = 0, nums[0]
        
#         while left < right:
#             left += 1
#             if right < left + nums[left]:
#                 right = left + nums[left]
            
#             if right >= len(nums)-1:
#                 return True
#         return False