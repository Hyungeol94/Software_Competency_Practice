class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_lowest_price = float("inf")
        left_largest_price = -1
        left_max_profit = 0
        left_max_profits = [-1 for i in range(len(prices))]

        right_lowest_price = float("inf")
        right_largest_price = -1
        right_max_profit = 0
        right_max_profits = [-1 for i in range(len(prices))]

        left = 0
        right = 0
        maxProfit = 0
        maxPrice = 0

        while right != len(prices):
            maxProfit = max(maxProfit, prices[right]-prices[left])
            left_max_profits[right] = maxProfit
            if prices[left] > prices[right]: #더 작은 것 발견했을 때의 처리
                left = right
            right += 1

        left = len(prices)-1
        right = len(prices)-1
        maxProfit = 0

        while left!= -1:
            maxProfit = max(maxProfit, prices[right]-prices[left])
            right_max_profits[left] = maxProfit
            if prices[right] < prices[left]:
                right = left
            left -= 1

        
        max_profit = -1
        
        for i, [left_profit, right_profit] in enumerate(
            zip(left_max_profits[:-1], right_max_profits[1:])
        ):
            print(left_profit, right_profit)
            max_profit = max(max_profit, left_profit+right_profit)
        max_profit = max(max_profit, left_max_profits[-1])
        return max_profit
