#https://leetcode.com/problems/find-the-safest-path-in-a-grid?envType=daily-question&envId=2026-07-01
#Find the Safest Path in a Grid
from collections import deque

class Solution:
    def getSafenessFactor(self, grid):
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        myqueue = deque()
        
        # 1. Enqueue ALL thieves at the start (Multi-source)
        # single-source로 여러번 하면 TLE
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    myqueue.append((i, j, 0))
                    dp[i][j] = 0 # Distance to a thief is 0
                    
        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Run a single BFS
        # Dijkstra와 유사
        while myqueue:
            i, j, depth = myqueue.popleft() #depth는 거기까지 가는 경로
            
            for dr in drs:
                next_i, next_j = i + dr[0], j + dr[1]
                
                if 0 <= next_i < n and 0 <= next_j < n:
                    # If we found a strictly shorter path to this cell, update and queue it
                    if dp[next_i][next_j] > depth + 1:
                        dp[next_i][next_j] = depth + 1
                        myqueue.append((next_i, next_j, depth + 1))
                        
        return dp

    #여기를 dfs로 하지 말고 bfs로 해도 되는 것임 (힌트처럼)

    def bfs(self, grid, dp, min_bound):
        seen = set([(0, 0)])
        myqueue = deque([(0, 0)])
        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)
        while myqueue:
            curr = myqueue.popleft()
            if curr[0] == n-1 and curr[1]== n-1:
                return True
            
            for dr in drs:
                next_i, next_j = curr[0]+dr[0], curr[1]+dr[1]
                if not (0<= next_i < n and 0<= next_j < n):
                    continue
                if dp[next_i][next_j] < min_bound:
                    continue
                if (next_i, next_j) in seen:
                    continue
                seen.add((next_i, next_j))
                myqueue.append((next_i, next_j))

        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = self.getSafenessFactor(grid)
        maxVal = 0
        for i in range(n):
            for j in range(n):
                maxVal = max(maxVal, dp[i][j])

        #경로를 기억해야 하므로 dfs
        #maximize the minimum => binary search
        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        left = 0
        right = maxVal
        max_factor = 0
        while left < right: #maximize the minimum
            mid = (left + right + 1) // 2
            seen = set([(0, 0)])
            mystack = [(0, 0)]
            # if mid == 0 or dp[0][0] >= mid and self.dfs(mystack, seen, drs, dp, n, grid, mid):
            if mid == 0 or dp[0][0] >= mid and self.bfs(grid, dp, mid):
                max_factor = mid
                left = mid
            else:
                right = mid-1

        return max_factor