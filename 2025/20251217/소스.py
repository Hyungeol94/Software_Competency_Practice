#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/description/?envType=daily-question&envId=2025-12-17
#3573. Best Time to Buy and Sell Stock V

from functools import lru_cache

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @lru_cache(maxsize=100000)
        def dp(state, i, k): #state 압축
            if state == 0:
                if i == n-1:
                    return 0

                res1 = -prices[i]+dp(1, i+1, k-1) if k >= 1 else -float('inf') #start normal transaction 
                res2 = prices[i]+dp(2, i+1, k-1) if k >= 1 else -float('inf') #start short transaction
                res3 = dp(0, i+1, k) #넘기기
                return max(res1, res2, res3)
            
            elif state == 1:
                if i == n-1:
                    return prices[i]
                
                res1 = prices[i] + dp(0, i+1, k) #end transaction 
                res2 = dp(1, i+1, k) #넘기기
                return max(res1, res2)
            
            else:
                if i == n-1:
                    return -prices[i]
                
                res1 = -prices[i] + dp(0, i+1, k)
                res2 = dp(2, i+1, k)
                return max(res1, res2)


        return dp(0, 0, k)
    
    from functools import lru_cache

    def maximumProfit_MLE(self, prices: List[int], k: int) -> int:
        #비싼값에 팔고 나중에 다시 사거나
        #싸게 사서 비싼값에 팔거나
        n = len(prices)

        @lru_cache(maxsize=50000)
        def dp(on_transaction, i, j, k):
            if not on_transaction:
                if i == n-1:
                    return 0

                res1 = dp(True, i+1, i, k-1) if k >= 1 else -float('inf') #start transaction 
                res2 = dp(False, i+1, j, k) #넘기기
                return max(res1, res2)
            
            else: #on_transaction
                if i == n-1:
                    #여기서 끝내기
                    profit = abs(prices[i]-prices[j])
                    return profit
                
                profit = abs(prices[i]-prices[j])

                res1 = (profit + dp(False, i+1, -1, k)) if profit >= 0 else -float('inf')  #transaction 완
                res2 = dp(True, i+1, j, k) #다음으로 미루기
                return max(res1, res2)


        return dp(False, 0, -1, k)