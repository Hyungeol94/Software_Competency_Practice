#https://leetcode.com/problems/last-day-where-you-can-still-cross/?envType=daily-question&envId=2025-12-31
#1970. Last Day Where You Can Still Cross

from collections import deque

class Solution:
    def is_valid(self, matrix, i, j):
        n = len(matrix)
        m = len(matrix[0])
        if 0 <= i < n and 0 <= j < m:
            return True
        return False

    def bfs(self, row, col, cells, k):
        matrix = [[0 for _ in range(col)] for _ in range(row)]
        for i, cell in enumerate(cells):
            matrix[cell[0]-1][cell[1]-1] = 1
            if i == k:
                break

        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False for _ in range(col)] for _ in range(row)]
        myqueue = deque([])
        for j in range(col):
            if matrix[0][j] != 1:
                myqueue.append((0, j))
                visited[0][j] = True

        while myqueue:
            curr = myqueue.popleft()
            i, j = curr
            if i == row-1:
                return True
            for dr in drs:
                i_offset, j_offset = dr
                next_i, next_j = i+i_offset, j+j_offset
                if not self.is_valid(matrix, next_i, next_j):
                    continue
                if visited[next_i][next_j]:
                    continue
                if matrix[next_i][next_j]:
                    continue
                visited[next_i][next_j] = True
                myqueue.append((next_i, next_j))
        return False
            

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left = 0
        right = len(cells)-1
        latestDay = 0
        while left <= right:
            mid = (left + right) // 2
            if self.bfs(row, col, cells, mid):
                latestDay = mid
                left = mid+1
            else:
                right = mid-1
        
        return latestDay+1