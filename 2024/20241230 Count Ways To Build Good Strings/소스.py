from functools import lru_cache

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @lru_cache(maxsize=5000)
        def dp(i):
            val = 0
            if low <= i <= high:
                val += 1
            
            if i + zero <= high:
                val += dp(i + zero)
            
            if i + one <= high:
                val += dp( i + one)
            
            return val

        return dp(0) % (10**9 + 7)