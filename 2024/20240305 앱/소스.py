#https://www.acmicpc.net/problem/7579

import sys
input = sys.stdin.readline
class Solution():
    def minCost(self, n, k, memories, costs):
        if n == 1:
            if k <= memories[0]:
                return costs[0]
            return float('inf')

        dp = [[[0, 0] for _ in range(10001)] for _ in range(n)]
        for costSum in range(10001):
            dp[0][costSum][0] = 0
            dp[0][costSum][1] = memories[0] if costs[0] <= costSum else 0

        for i in range(1, n):
            for costSum in range(10001):
                #if state == 0
                dp[i][costSum][0] = max(dp[i-1][costSum][0], dp[i-1][costSum][1])

                #if state == 1
                if 0 <= costSum-costs[i]:
                    dp[i][costSum][1] = max(dp[i-1][costSum-costs[i]][0]+memories[i],
                                            dp[i-1][costSum-costs[i]][1]+memories[i])

        #top-down 점화식
        # def dp(i, costSum, state):
        #     if i == 0:
        #         if state == 0:
        #             return 0
        #         return memories[0]
        #
        #     if state == 0:
        #         return max(dp(i-1, costSum, 0), dp(i-1, costSum, 1))
        #     return max(dp(i - 1, costSum - costs[i], 0) + memories[i],
        #                dp(i - 1, costSum - costs[i], 1) + memories[i])

        minCost = float('inf')
        for i in range(n):
            for costSum in range(10001):
                if k <= dp[i][costSum][0]:
                    minCost = min(minCost, costSum)
                if k <= dp[i][costSum][1]:
                    minCost = min(minCost, costSum)
        return minCost


instance = Solution()
n, k = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(instance.minCost(n, k, memories, costs))