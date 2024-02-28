
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, hold):
            if i == 0:
                if hold:
                    return -float('inf')
                else:
                    return 0

            if hold:
                return max(dp(i-1, False)-prices[i-1], dp(i-1, True))
            else:
                return max(dp(i-1, True)+prices[i-1]-fee, dp(i-1, False))

        return max(dp(len(prices), False), dp(len(prices), True))