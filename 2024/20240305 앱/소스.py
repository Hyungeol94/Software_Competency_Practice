#https://www.acmicpc.net/problem/7579

from functools import cache
class Solution():
    def minCost(self, n, k, memories, costs):
        if n == 1:
            if k <= memories[0]:
                return costs[0]
            return float('inf')

        @cache
        def dp(i, k, state):
            if i == 0:
                if state == 0: #선택하지 않음
                    if k <= 0:
                        return 0
                    return float('inf')
                else:
                    if k-memories[0] <= 0:
                        return costs[0]
                    return float('inf')
            else:
                return min(costs[i]+dp(i-1, k-memories[i], 1), dp(i-1, k, 0))
        return min(costs[n-1]+dp(n-1, k-memories[n-1], 1), dp(n-1, k, 0))



instance = Solution()
n, k = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(instance.minCost(n, k, memories, costs))