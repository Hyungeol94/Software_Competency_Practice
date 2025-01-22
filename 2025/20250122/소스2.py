#https://leetcode.com/problems/map-of-highest-peak/description/
#1765. Map of Highest Peak

import heapq

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        heap = []
        heapq.heapify(heap)

        matrix = [[0]*m for _ in range(n)]
        visited = [[False]*m for _ in range(n)]


        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    heapq.heappush(heap, (0, i, j))

        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while heap:
            height, row, col = heapq.heappop(heap)
            if visited[row][col]:
                continue
            visited[row][col] = True
            matrix[row][col] = height

            for row_offset, col_offset in drs:
                nr, nc = row+row_offset, col+col_offset
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if visited[nr][nc]:
                    continue
                heapq.heappush(heap, (height+1, nr, nc))

        return matrix