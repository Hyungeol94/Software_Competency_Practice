#https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(amount, i):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if i == -1:
                return 0
            sum = 0
            for i in range(i+1):
                coin = coins[i]
                for j in range(1, amount//coin+1):
                    sum += dp(amount-j*coin, i-1)
            return sum
        return dp(amount, len(coins)-1)
        