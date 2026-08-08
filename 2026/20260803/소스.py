#https://leetcode.com/problems/stone-game-iii/description/?envType=daily-question&envId=2026-08-03
#1406. Stone Game III

from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        @cache
        def dp(state, i):
            if i >= n:
                return 0
            
            if state:
                val1 = sum(stoneValue[i: i+1]) + dp(not state, i+1)
                val2 = sum(stoneValue[i: i+2]) + dp(not state, i+2)
                val3 = sum(stoneValue[i: i+3]) + dp(not state, i+3)
                return max(val1, val2, val3)
            
            else:
                val1 = -sum(stoneValue[i: i+1]) + dp(not state, i+1)
                val2 = -sum(stoneValue[i: i+2]) + dp(not state, i+2)
                val3 = -sum(stoneValue[i: i+3]) + dp(not state, i+3)
                return min(val1, val2, val3)
        
        res = dp(True, 0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"