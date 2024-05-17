class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -(10 ** 5)
        temp, partial = 0, -(10 ** 5)
        
        for i in range(len(nums)):
            if nums[i] <= 0 and nums[i] > result:
                result = nums[i]
                
            if nums[i] <= 0 and temp + nums[i] >= 0:
                temp += nums[i]
                partial = temp
            elif nums[i] <=0 and temp + nums[i] < 0:
                temp = 0
            elif nums[i] > 0:
                temp += nums[i]
                partial = temp
            
            if partial > result:
                result = partial
                
        return result