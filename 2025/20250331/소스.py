#https://leetcode.com/problems/put-marbles-in-bags/?envType=daily-question&envId=2025-03-31
#2551. Put Marbles in Bags

from functools import cache
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        @cache #일단 최댓값 계산 먼저
        def max_dp(i, k):
            if k == 1:
                if n <= i:
                    return -float('inf')
                else:
                    return weights[i]+weights[n-1]
        
            else:
                maxVal = -float('inf')
                for j in range(i, n):
                    #앞부분
                    maxVal = max(maxVal, weights[i] + weights[j] + max_dp(j+1, k-1))
                return maxVal
        
        
        @cache
        def min_dp(i, k):
            if k == 1:
                if n <= i :
                    return float('inf')
                else:
                    return weights[i]+weights[n-1]
            
            else:
                minVal = float('inf')
                for j in range(i, n):
                    minVal = min(minVal, weights[i] + weights[j] + min_dp(j+1, k-1))
                return minVal
        
        return max_dp(0, k) - min_dp(0, k)
