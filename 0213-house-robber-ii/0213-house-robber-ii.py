class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        
        def helper(nums):
            if len(nums) < 2:
                return max(nums)

            dp = [nums[0],max(nums[0], nums[1])]

            for i in range(2,len(nums)):
                dp.append(max(dp[-2]+nums[i], dp[-1]))

            return max(dp)
        
        return max(helper(nums[1:]), helper(nums[:-1]))