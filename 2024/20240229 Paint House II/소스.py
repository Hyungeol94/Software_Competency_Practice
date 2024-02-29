#https://leetcode.com/problems/paint-house-ii/description/

from functools import cache

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])

        @cache
        def dp(i, color):
            if i == 0:
                return costs[0][color]
            
            else:
                adjacentColors = [adjColor for adjColor in range(k) if adjColor!=color]
                minCost = float('inf')
                for adjacentColor in adjacentColors:
                    minCost = min(minCost, dp(i-1, adjacentColor)+costs[i][color])
                return minCost

        minCost = float('inf')
        for color, cost in enumerate(costs[-1]):
            minCost = min(minCost, dp(n-1, color))
        return minCost
    
        