#https://leetcode.com/problems/minimum-cost-path-with-teleportations/?envType=daily-question&envId=2026-01-28
#3651. Minimum Cost Path with Teleportations

import heapq
from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[float('inf') for _ in range(n)] for _ in range(m)] for _ in range(k+1)]
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0, 0))
        drs = [(1, 0), (0, 1)]
        for i in range(k+1):
            dp[i][0][0] = 0
        
        for move_count in range(k+1):
            #heap 한번 돌기
            while heap:
                cost, i, j = heapq.heappop(heap)
                if cost > dp[move_count][i][j]:
                    continue

                #normal move
                for dr in drs:
                    x_offset, y_offset = dr
                    if not (0 <= i+x_offset < m and 0 <= j+y_offset < n):
                        continue
                    next_cost = cost + grid[i+x_offset][j+y_offset]
                    if next_cost < dp[move_count][i+x_offset][j+y_offset]:
                        dp[move_count][i+x_offset][j+y_offset] = next_cost
                        heapq.heappush(heap, (next_cost, i+x_offset, j+y_offset))

            
            if move_count == k:
                break
            
            #다음 teleportation 계산해 넣기
            min_cost_per_value = defaultdict(lambda: float('inf'))
            for i in range(m):
                for j in range(n):
                    value = grid[i][j]
                    min_cost_per_value[value] = min(min_cost_per_value[value], dp[move_count][i][j])

            grid_values = sorted(min_cost_per_value.keys(), reverse=True)
            min_cost_suffix = {}
            min_val = float('inf')
            
            for value in grid_values:
                min_val = min(min_val, min_cost_per_value[value])
                min_cost_suffix[value] = min_val
            
            new_heap = []
            heapq.heapify(new_heap)
            for i in range(m):
                for j in range(n):
                    value = grid[i][j]
                    dp[move_count+1][i][j] = min_cost_suffix[value]
                    heapq.heappush(new_heap, (min_cost_suffix[value], i, j))
            
            heap = new_heap
 
        
        minVal = float('inf')
        for i in range(k+1):
            minVal = dp[i][m-1][n-1]
        return minVal
    

class Solution_TLE:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        points = defaultdict(list)
        for i in range(m):
            for j in range(n):
                points[grid[i][j]].append((i, j))

        keys = sorted(list(points.keys())) 
        dp = [[[float('inf') for _ in range(n)] for _ in range(m)] for _ in range(k+1)]
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0, 0, 0))
        drs = [(1, 0), (0, 1)]
        for i in range(k+1):
            dp[i][0][0] = 0
        
        while heap:
            cost, i, j, move_count = heapq.heappop(heap)
            if cost > dp[move_count][i][j]:
                continue

            #normal move
            for dr in drs:
                x_offset, y_offset = dr
                if not (0 <= i+x_offset < m and 0 <= j+y_offset < n):
                    continue
                next_cost = cost + grid[i+x_offset][j+y_offset]
                if next_cost < dp[move_count][i+x_offset][j+y_offset]:
                    dp[move_count][i+x_offset][j+y_offset] = next_cost
                    heapq.heappush(heap, (next_cost, i+x_offset, j+y_offset, move_count))
            
            #teleportation
            if move_count >= k:
                continue

            curr = grid[i][j]
            upper_bound = bisect.bisect_left(keys, curr)
            for index in range(upper_bound+1):
                key = keys[index]
                for point in points[key]:
                    p, q = point
                    if cost < dp[move_count+1][p][q]:
                        dp[move_count+1][p][q] = cost
                        heapq.heappush(heap, (cost, p, q, move_count+1))

        
        minVal = float('inf')
        for i in range(k+1):
            minVal = dp[i][m-1][n-1]
        return minVal