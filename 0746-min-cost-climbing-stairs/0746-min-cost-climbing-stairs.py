class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:2]
        
        for i in range(2, len(cost)):
            dp.append(min(cost[i]+dp[i-1], cost[i]+dp[i-2]))
                      
        return min(dp[-1], dp[-2])