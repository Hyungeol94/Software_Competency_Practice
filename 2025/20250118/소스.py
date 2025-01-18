from typing import List
from collections import deque
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        #다익스트라 알고리즘
        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[float('inf')]*n for _ in range(m)]
        heap = []
        heapq.heapify(heap)
        dp[0][0] = 0
        heapq.heappush(heap, [0, 0, 0])

        while heap:
            cost, i, j = heapq.heappop(heap)
            for index, dr in enumerate(drs):
                row_offset, col_offset = dr
                next_row = i+row_offset
                next_col = j+col_offset
                if not (0 <= next_row < m and 0 <= next_col < n):
                    continue
                
                next_cost = cost
                if index+1 != grid[i][j]:
                    next_cost += 1
                
                if next_cost < dp[next_row][next_col]:
                    dp[next_row][next_col] = next_cost
                    heapq.heappush(heap, [next_cost, next_row, next_col])

        return dp[m-1][n-1]