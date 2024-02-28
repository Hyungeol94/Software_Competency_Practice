from functools import cache

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @cache
        def dp(i, color):
            if i == 0:
                return costs[i][color]
            
            if color == 0:
                return costs[i][color]+min(dp(i-1, 1), dp(i-1, 2))
            elif color == 1:
                return costs[i][color]+min(dp(i-1, 0), dp(i-1, 2))
            else:
                return costs[i][color]+min(dp(i-1, 0), dp(i-1, 1))

        return min(dp(n-1, 0), dp(n-1, 1), dp(n-1, 2))
        