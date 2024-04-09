#https://leetcode.com/problems/rotting-oranges/
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        targets = 0
        myqueue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    targets += 1
                if grid[i][j] == 2:
                    myqueue.append([0, i, j])
        
        if targets == 0:
            return 0
        
        row_offsets = [0, 1, 0, -1]
        col_offsets = [1, 0, -1, 0]

        count = 0
        while myqueue:
            depth, i, j = myqueue.popleft()
            for row_offset, col_offset in zip(row_offsets, col_offsets):
                next_row = i+row_offset
                next_col = j+col_offset
                if 0<=next_row<=n-1 and 0<=next_col<=m-1:
                    if grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        count += 1
                        myqueue.append([depth+1, next_row, next_col])
                        if count == targets:
                            return depth+1
        return -1
    
                    
            
        
        

