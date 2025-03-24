#https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/?envType=daily-question&envId=2025-03-23
#1976. Number of Ways to Arrive at Destination

import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        MOD = 10**9 + 7

        #heap을 이용해서
        adj_list = defaultdict(list)
        for edge in roads:
            k, v, cost = edge
            adj_list[k].append([v, cost])
            adj_list[v].append([k, cost])
        
        #0에서 시작
        heap = []
        heapq.heapify(heap)
        costMap = [float('inf') for i in range(n)]
        pathCountDict = defaultdict(int)

        for edge in adj_list[0]:
            neighbor, cost = edge
            heapq.heappush(
                heap, [cost, neighbor]
            )
            pathCountDict[neighbor] = 1
            costMap[neighbor] = cost


        #heap으로 dijkstra's algorithm 적용
        while heap:
            cost, curr = heapq.heappop(heap)
            if curr == n-1:
                break
            
            else:
                for neighbor, offset in adj_list[curr]:
                    next_cost = (cost+offset)
                    if next_cost < costMap[neighbor]: 
                        heapq.heappush(heap, [next_cost, neighbor])
                        pathCountDict[neighbor] = pathCountDict[curr]
                        costMap[neighbor] = next_cost
                    elif next_cost == costMap[neighbor]:
                        pathCountDict[neighbor] += pathCountDict[curr]
        
        
        return pathCountDict[n-1] % MOD