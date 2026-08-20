#https://leetcode.com/problems/stone-game-v/submissions/2110720301/?envType=daily-question&envId=2026-08-17
#1563. Stone Game V

from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        acc = 0
        prefixSum = []
        for value in stoneValue:
            acc += value
            prefixSum.append(acc)
            
        @cache
        def dp(i, j):
            if i == j:
                return 0
                
            
            maxVal = -float('inf')
            for k in range(i, j):
                leftSum = prefixSum[k]-prefixSum[i-1] if i >= 1 else prefixSum[k]
                rightSum = prefixSum[j]-prefixSum[k]
                
                if leftSum > rightSum:
                    maxVal = max(maxVal, rightSum + dp(k+1, j))
                elif leftSum == rightSum:
                    maxVal = max(maxVal, rightSum + dp(k+1, j))
                    maxVal = max(maxVal, leftSum + dp(i, k))
                else:
                    maxVal = max(maxVal, leftSum + dp(i, k))
                    
            
            return maxVal
            
        return dp(0, len(stoneValue)-1)