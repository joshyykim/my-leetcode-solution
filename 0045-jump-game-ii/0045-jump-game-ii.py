class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) for j in range(len(nums)-1)]
        dp.insert(0,0)
        for i in range(len(nums)):
            for j in range(nums[i]+1):
                if (i+j) == len(nums):
                    break
                dp[i+j] = min(dp[i]+1,dp[i+j])
        return dp[-1]