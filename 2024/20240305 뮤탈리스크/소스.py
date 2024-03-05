
#
from functools import cache
class Solution():
    def minAttack(self, n, nums):
        if n == 3:
            @cache
            def dp(i, j, k):
                if i <= 0 and j <= 0 and k <= 0:
                    return 0
                return min(1+dp(i-9, j-3, k-1), 1+dp(i-9, j-1, k-3), 1+dp(i-3, j-9, k-1), 1+dp(i-1, j-9, k-3), 1+dp(i-3, j-1, k-9), 1+dp(i-1, j-3, k-9))
            return dp(*nums)
        if n == 2:
            @cache
            def dp(i, j):
                if i<=0 and j<=0:
                    return 0
                return min(1+dp(i-9, j-3), 1+dp(i-3, j-9))
            return dp(*nums)

        if n == 1:
            @cache
            def dp(i):
                if i <=0:
                    return 0
                return 1+dp(i-9)
            return dp(*nums)


instance = Solution()
n = int(input())
nums = list(map(int, input().split()))
print(instance.minAttack(n, nums))