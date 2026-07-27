#https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=daily-question&envId=2026-07-02
#3286. Find a Safe Walk Through a Grid

import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*m for _ in range(n)]
        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = []
        heapq.heapify(heap)
    
        heapq.heappush(heap, (-(health if not grid[0][0] else health-1), 0, 0))
        dp[0][0] = health if not grid[0][0] else health-1
        while heap:
            health, i, j = heapq.heappop(heap)
            health = -health
            for dr in drs:
                row_offset, col_offset = dr
                row, col = i+row_offset, j+col_offset
                if not (0 <= row < n and 0 <= col <m):
                    continue
                next_health = health if not grid[row][col] else health-1
                if dp[row][col] >= next_health:
                    continue
                dp[row][col] = next_health
                heapq.heappush(heap, (-next_health, row, col))

        return True if dp[n-1][m-1] else False
                
            
            
        