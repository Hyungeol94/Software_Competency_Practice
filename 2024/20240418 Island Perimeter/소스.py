from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        global perimeter
        perimeter = 0
        myqueue = deque([])
        row_offsets = [0, 1, 0, -1]
        col_offsets = [1, 0, -1, 0]
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]

        def isValid(i, j):
            if 0 <= i <= len(grid)-1 and 0 <= j <= len(grid[0])-1:
                return True
            return False

        def count_surroundings(i, j):
            count = 0 
            for row_offset, col_offset in zip(row_offsets, col_offsets):
                    next_row = i+row_offset
                    next_col = j+col_offset
                    
                    if isValid(next_row, next_col) and visited[next_row][next_col]:
                        count += 1
            return count
            

        def bfs():
            while myqueue:
                [i, j] = myqueue.popleft()
                global perimeter
                perimeter += 4-count_surroundings(i, j)

                for row_offset, col_offset in zip(row_offsets, col_offsets):
                    next_row = i+row_offset
                    next_col = j+col_offset
                    
                    if isValid(next_row, next_col) and not visited[next_row][next_col] and grid[next_row][next_col]:
                        myqueue.append([next_row, next_col])
                        visited[next_row][next_col] = True
                        perimeter -= 1

                    
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 1:
                    myqueue.append([i, j])
                    visited[i][j] = True 
                    bfs()
                    return perimeter
                    

    