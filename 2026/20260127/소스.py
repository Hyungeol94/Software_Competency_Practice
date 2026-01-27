#https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/?envType=daily-question&envId=2026-01-27
#3650. Minimum Cost Path with Edge Reversals

from collections import defaultdict
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)

        for edge in edges:
            u, v, w = edge
            neighbors[u].append((v, w))
            neighbors[v].append((u, 2*w))
        
        heap = []
        heapq.heapify(heap)

        dp = [float('inf') for _ in range(n)]
        
        for edge in neighbors[0]:
            neighbor, weight = edge
            if weight < dp[neighbor]:
                dp[neighbor] = weight
                heapq.heappush(heap, (neighbor, weight))
        
        while heap:
            curr, cost = heapq.heappop(heap)
            for edge in neighbors[curr]:
                neighbor, weight = edge
                if cost + weight < dp[neighbor]:
                    dp[neighbor] = cost+weight
                    heapq.heappush(heap, (neighbor, cost+weight))
        
        return dp[n-1] if dp[n-1] != float('inf') else -1