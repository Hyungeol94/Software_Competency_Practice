class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        right = 1
        while (right != len(prices)):
            maxProfit = max(maxProfit, prices[right]-prices[left])
            if prices[left] > prices[right]:
                left = right
            right += 1
        return maxProfit
            
            
                


        
