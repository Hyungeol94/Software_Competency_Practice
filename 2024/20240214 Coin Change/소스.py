#https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amount):
            if amount == 0:
                return 0
            if amount < min(coins):
                return -1
            
            output = float('inf')
            for coin in coins:
                output = min(output, 1+ dp(amount-coin)) if dp(amount-coin) != -1 else output
            
            return output if output != float('inf') else -1
        return dp(amount)
        