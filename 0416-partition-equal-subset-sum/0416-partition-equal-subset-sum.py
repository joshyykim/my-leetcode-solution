class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If total sum is odd, can't split into two subsets with equal sum
        if total % 2 != 0:
            return False

        target = total // 2

        # Use dynamic programming to check for a subset with sum equal to target
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
                
        return dp[target]