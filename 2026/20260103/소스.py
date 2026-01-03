#https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/?envType=daily-question&envId=2026-01-03
#1411. Number of Ways to Paint N × 3 Grid

class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dp(i, state):
            if i == n-1:
                if state == 1:
                    return 5
                else:
                    return 4
            
            else:
                if state == 1:
                    return (3*dp(i+1, 1)+2*dp(i+1, 2)) % mod
                else:
                    return (2*dp(i+1, 1)+2*dp(i+1, 2)) % mod
            
        if n == 1:
            return 12
        else:
            return (6 * dp(1, 1) + 6 * dp(1, 2)) % mod
                