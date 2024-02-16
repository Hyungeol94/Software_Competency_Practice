#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, state) -> int:
            if i == 0:
                if state == 1:
                    return -prices[0]
                else:
                    return 0

            if state == 1: #holding
                profitBeforeBuying = dp(i-1, 3)
                profitBeforeWitholding = dp(i-1, 1)
                return max(profitBeforeBuying-prices[i-1], profitBeforeWitholding)
            
            if state == 2: #not holding + cooltime
                profitBeforeSelling = dp(i-1, 1)
                return profitBeforeSelling+prices[i-1] if i-1 != 0 else 0
            
            if state == 3: #not holding + cooltime finished
                profitBeforeWaiting = dp(i-1, 3)
                profitBeforeCoolingDown = dp(i-1, 2)
                return max(profitBeforeWaiting, profitBeforeCoolingDown)

        
        return max(dp(len(prices), 2), dp(len(prices), 3))
