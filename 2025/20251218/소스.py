#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/?envType=daily-question&envId=2025-12-18
#3652. Best Time to Buy and Sell Stock using Strategy

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        acc = 0
        for price, action in zip(prices, strategy):
            if action == -1:
                acc -= price
            elif action == 1:
                acc += price
            else:
                continue

        #왼쪽, 가운데, 오른쪽만 바꿔가면서 slide하면 됨
        #가운데가 두 번 계산되지 않도록 해야함

        mid = k // 2
        acc2 = 0
        i = 0
        while i < mid:
            i += 1
        
        while i < k: 
            acc2 += prices[i]
            i += 1

        while i < len(prices):
            price, action = prices[i], strategy[i]
            if action == -1:
                acc2 -= price
            elif action == 1:
                acc2 += price
            i += 1 

        acc = max(acc, acc2)
            
        left = 0
        mid = left + k // 2 #right의 끝
        right = k-1
        n = len(prices)

        left += 1
        mid += 1
        right += 1

        while right < n:
            #window 바깥에 있던 것이 right window에 들어가게 됨
            right_price, right_action = prices[right], strategy[right]
            if right_action == -1:
                acc2 += right_price * 2
            elif right_action == 0:
                acc2 += right_price

            #mid가 left window에 들어가게 됨
            mid_price, mid_action = prices[mid-1], strategy[mid-1]
            acc2 -= mid_price

            #left가 window에서 제외됨 => 0에서 원래대로 복구
            left_price, left_action = prices[left-1], strategy[left-1]
            if left_action == -1:
                acc2 -= left_price
            elif left_action == 1:
                acc2 += left_price

            left += 1
            mid += 1
            right += 1
            
            acc = max(acc, acc2)
        
        return acc
