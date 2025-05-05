#https://leetcode.com/problems/domino-and-tromino-tiling/?envType=daily-question&envId=2025-05-05
#790. Domino and Tromino Tiling

from functools import cache

class Solution:
    @cache
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(i, state):
            if i > n:
                return 0

            if i == n:
                if state == 0:
                    return 1
                else:
                    return 0
            
            else:
                if state == 0:
                    return (dp(i+1, 0)+ dp(i+2, 0) + 2*dp(i+1, 1)) % MOD
                
                else:
                    return (dp(i+2, 0) + dp(i+1, 1)) % MOD
        
        return dp(0, 0) % MOD