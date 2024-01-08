class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sumProfit = 0
        currentProfit = 0
        cost = 10**4+1
        left = 0
        right = 1
        while right != len(prices):
            if prices[left] < cost:
                cost = prices[left]
            if currentProfit < prices[right]-prices[left]:
                currentProfit = prices[right]-prices[left]
                if right == len(prices)-1:
                    sumProfit += currentProfit
            else:
                sumProfit += currentProfit
                currentProfit = 0
                left = right
            right += 1
        return sumProfit



        
            