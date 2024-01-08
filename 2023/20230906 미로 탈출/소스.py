from collections import deque

def is_valid(x, y, maps):
    if y< 0 or len(maps)<=y:
        return False
    if x< 0 or len(maps[0])<=x:
        return False
    return True

def passable(row, col, maps):
    if maps[row][col] != 'X':
        return True
    else:
        return False
    

def bfs(q, end, maps):
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    dys = [0, -1, 0, 1]
    dxs = [1, 0, -1, 0]
    
    while q:
        *current, depth = q.popleft()
        if current == end:
            return depth
        
        row, col = current
        for dy, dx in zip(dys, dxs):
            next_row = row+dy
            next_col = col+dx
            if is_valid(next_col, next_row, maps) and not visited[next_row][next_col]:
                if passable(next_row, next_col, maps):
                    q.append([next_row, next_col, depth+1])
                    visited[next_row][next_col] = True
    return -1
        
                
def solution(maps):
    start_position = []
    lever_position = []
    destination = []
    for i, row in enumerate(maps):
        for j, mark in enumerate(row):
            if mark == 'S':
                start_position = [i, j]
            if mark == 'L':
                lever_position = [i, j]
            if mark == 'E':
                destination = [i, j]
    #레버에 먼저 도착 
    q = deque([[*start_position, 0]])
    count = bfs(q, lever_position, maps)
    if count == -1:
        return -1
    
    #다시 bfs를 하기
    q = deque([[*lever_position, 0]])
    result = bfs(q, destination, maps)
    count = -1 if result == -1 else count+result
    return count
  