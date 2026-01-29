#https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2026-01-29
#2976. Minimum Cost to Convert String I

from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        #all path shortest costs 구하기 => 플로이드 워셜
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        n = len(alphabets)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for o, c, cost in zip(original, changed, cost):
            i, j = ord(o)-ord('a'), ord(c)-ord('a')
            dp[i][j] = min(dp[i][j], cost)

        heap = []
        heapq.heapify(heap)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if k == i or k == j:
                        continue
                    if dp[i][k]+dp[k][j] >= dp[i][j]:
                        continue
                    dp[i][j] = dp[i][k]+dp[k][j]
                    heapq.heappush(heap, (dp[i][j], i, j))
                    

        while heap:
            cost, i, j = heapq.heappop(heap)
            if cost != dp[i][j]:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                if dp[i][k]+dp[k][j] >= dp[i][j]:
                    continue
                dp[i][j] = dp[i][k]+dp[k][j]
                heapq.heappush(heap, (dp[i][j], i, j))


        costs = 0
        for o, c in zip(source, target):
            i, j = ord(o)-ord('a'), ord(c)-ord('a')
            costs += dp[i][j]
        
        return costs if costs != float('inf') else -1