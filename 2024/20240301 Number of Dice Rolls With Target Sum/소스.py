#https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(i, target):
            if i == 1:
                if 1<= target <= k:
                    return 1
                else:
                    return -float('inf')

            else:
                count = 0
                for j in range(1, k+1):
                    count = count+dp(i-1, target-j) if dp(i-1, target-j)!=-float('inf') else count
                return count
                
        return dp(n, target) % (10**9+7)
                
                
        