from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        myqueue = deque([[1, 0, 0]])
        x_offsets = [1, 1, 1, 0, -1, -1, -1, 0]
        y_offsets = [-1, 0, 1, 1, 1, 0, -1, -1]
        visited = [[False]*n for _ in range(n)]
        visited[0][0] = True
        
        if grid[0][0] == 1:
            return -1

        while myqueue:
            depth, i, j = myqueue.popleft()
            if i == n-1 and j == n-1:
                return depth
            for x_offset, y_offset in zip(x_offsets, y_offsets):
                next_x = j+x_offset
                next_y = i+y_offset
                if 0 <= next_x <= n-1 and 0 <= next_y <= n-1 and not visited[next_y][next_x] and grid[next_y][next_x] == 0:
                    myqueue.append([depth+1, next_y, next_x])
                    visited[next_y][next_x] = True
        return -1