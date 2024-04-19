from collections import deque

class Solution:
    def isValid(self, i, j, grid):
        n = len(grid)
        m = len(grid[0])
        if 0 <= i <= n-1 and 0 <= j <= m-1:
            return True
        return False

    def numIslands(self, grid: List[List[str]]) -> int:
        row_offsets = [0, 1, 0, -1]
        col_offsets = [1, 0, -1, 0]
        def bfs(point):
            myqueue = deque([point])
            while myqueue:
                row, col = myqueue.popleft()
                for row_offset, col_offset in zip(row_offsets, col_offsets):
                    next_row = row+row_offset
                    next_col = col+col_offset
                    if self.isValid(next_row, next_col, grid) and grid[next_row][next_col] == "1":
                        myqueue.append([next_row, next_col])
                        grid[next_row][next_col] = "0"
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    bfs([i, j])
                    count += 1 
        
        return count      
                