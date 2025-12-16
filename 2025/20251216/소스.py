#https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/?envType=daily-question&envId=2025-12-16
#3562. Maximum Profit from Trading Stocks with Discounts

from functools import cache
from collections import defaultdict
from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        #직속상관에 관해서만 할인해 줌
        children = defaultdict(list)
        for k, v in hierarchy:
            children[k-1].append(v-1)
        
        @cache
        def dp(i, is_sale, budget): 
            #i를 루트로 갖는 트리에 대해 budget 내에서 최고의 profit을 구하기
            #is_sale은 직속상관이 구매를 했었는지 여부

            price = present[i] if not is_sale else present[i] // 2
            profit = future[i] - price
            
            #leaf일 때
            if not children[i]: 
                if price <= budget:
                    if 0 <= profit:
                        return (price, profit)
                    else:
                        return (0, 0)
                else: #살 수 없음
                    return (price, 0)
            
            #leaf가 아닐 때
            #구매
            res1 = dp2(i, 0, True, budget-price)
            ans1 = (price + res1[0], profit + res1[1])

            #구매X
            res2 = dp2(i, 0, False, budget)
            ans2 = res2

            return ans1 if ans1[1] >= ans2[1] else ans2
                
        
        @cache
        def dp2(p, i, is_sale, budget):
            #직속상관은 바뀌지 않으므로 일관되게 유지
            #buy-or-not 
            if budget < 0:
                return (float('inf'), -float('inf'))
            
            if budget == 0:
                return (0, 0)
            
            m = len(children[p])
            if i == m-1:
                price, profit = dp(children[p][i], is_sale, budget)
                if price <= budget: 
                    res = (price, profit)
                else:
                    res = (0, 0)
                return res

            maxVal = (0, 0)
            for j in range(budget+1):
                price, profit = dp(children[p][i], is_sale, j)
                
                res1 = dp2(p, i+1, is_sale, budget)
                ans1 = res1
                res2 = dp2(p, i+1, is_sale, budget-price)
                ans2 = (price + res2[0], profit+res2[1])
                
                res = ans1 if ans1[1] >= ans2[1] else ans2
                maxVal = res if res[1] > maxVal[1] else maxVal
            
            return maxVal


        res = dp(0, False, budget)
        return res[1]