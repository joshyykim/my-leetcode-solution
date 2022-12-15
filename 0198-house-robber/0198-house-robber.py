class Solution:
    def rob(self, nums: List[int]) -> int:
        lnh = len(nums)
        if lnh < 2: return max(nums)
        dp = [[0 for _ in range(lnh)] for _ in range(lnh)]
        for i in range(2):
            for j in range(i,lnh):
                dp[i][j] = nums[i]
        for i in range(2, lnh):
            max_col = 0
            for j in range(i-1):
                if max_col < dp[j][i]:
                    max_col = dp[j][i]
            for k in range(i,lnh):
                dp[i][k] = max_col + nums[i]
        return max(dp[-1][-1], dp[-2][-1])