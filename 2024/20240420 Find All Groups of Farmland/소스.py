from collections import deque
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        myqueue = []
        row_offsets = [1, 0]
        col_offsets = [0, 1]
        m = len(land[0])
        n = len(land)
        visited = [[False]*m for _ in range(n)]
        answer = []
        def bfs(point):
            myqueue = deque([point])
            visited[point[0]][point[1]] = True
            last_point = point
            while myqueue:
                i, j = myqueue.popleft()
                last_point = [i, j]
                for row_offset, col_offset in zip(row_offsets, col_offsets):
                    next_row = i+row_offset
                    next_col = j+col_offset
                    if not (0 <= next_row <=n-1 and 0<= next_col<=m-1):
                        continue
                    if visited[next_row][next_col]:
                        continue
                    if land[next_row][next_col] == 0:
                        continue
                    myqueue.append([next_row, next_col])
                    visited[next_row][next_col] = True
            answer.append([*point, *last_point])

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and not visited[i][j]:
                    bfs([i, j])

        return answer
                
        
                    
                    

               
                
                
            
