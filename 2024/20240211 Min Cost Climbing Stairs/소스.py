#Min Cost Climbing Stairs
#https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dp(i):
            if i == 1:
                return cost[0]
            if i == 2:
                return min(cost[1], cost[0])
            
            for j in range(3, n+1):
                if j not in memo:
                    memo[j] = min(cost[j-1]+memo[j-2], cost[j-1]+memo[j-1])
            
            return min(memo[i], memo[i-1])

        memo = {}
        memo[1] = cost[0] 
        memo[2] = cost[1]
        return dp(n)

            
                
        