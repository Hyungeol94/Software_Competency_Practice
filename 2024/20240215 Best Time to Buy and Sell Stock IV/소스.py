#

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def dp(i, holding, transactions):
            if i == 0:
                # return 0
                if holding == True:
                    return -prices[0]
                else:
                    return 0
           
            if holding: #이미 산 상태 -> 현재 갖고 있음
                #이미 사둔 걸 계속 갖고 있을 때
                beforeKept = dp(i-1, True, transactions) 
                #바로 이전에 샀을 때
                beforeBought = dp(i-1, False, transactions-1)
                return max(beforeBought-prices[i-1], beforeKept)
            
            else: #안갖고 있는 상태
                #이전에도 안갖고 있었을 때
                beforeWaiting = dp(i-1, False, transactions)
                if transactions == 0: #더 살 수 없음
                    return beforeWaiting
                #바로 이전에 팔았을 때
                beforeSold = dp(i-1, True, transactions)
                return max(beforeWaiting, beforeSold+prices[i-1])
        
        not_holding = dp(len(prices), False, k)
        holding = dp(len(prices), True, k)
        return  max(not_holding, holding)

        