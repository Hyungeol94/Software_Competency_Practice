class Solution:
    profit = -1
    def maxProfit(self, prices: List[int]) -> int:
        for i, purchasePrice in enumerate(prices):
            for j, sellingPrice in enumerate(prices[i:]):
                self.profit = max(self.profit, sellingPrice-purchasePrice)
        return self.profit
            
                
    #사는 시점에서는 파는 시점이 미래여야 함