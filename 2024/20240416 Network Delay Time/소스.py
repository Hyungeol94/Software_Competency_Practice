import heapq
from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Dijkstra's Algorithm
        #값이 더 작을 때만 테이블 업데이트하기!!
        #non-negative edge임이 보장됨 -> 사이클이 있어도 queue에 들어가지 않음
        weights = [[float('inf')]*(n+1) for _ in range(n+1)]
        adjList = [[] for _ in range(n+1)]
        costs = [float('inf')]*(n+1)
        costs[k] = 0
        costs[0] = 0

        for time in times:
            u, v, w = time
            adjList[u].append(v)
            weights[u][v] = w
        
        q = [[0, k]]
        heapq.heapify(q)
        while q:
            cost, curr = heapq.heappop(q)
            for next_node in adjList[curr]:
                weight = weights[curr][next_node]
                if cost+weight < costs[next_node]:
                    costs[next_node] = cost+weight
                    heapq.heappush(q, [cost+weight, next_node])

        cost = max(costs)
        return cost if cost!=float('inf') else -1
