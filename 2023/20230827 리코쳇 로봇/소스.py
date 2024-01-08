#https://school.programmers.co.kr/learn/courses/30/lessons/169199
from collections import deque
def get_next_positions(origin_row, origin_col, board):
    next_positions = []
    #상
    current_row, current_col = origin_row, origin_col
    next_col = origin_col
    while True:
        next_row = current_row -1
        #벽이나 장애물에 부딪혔을 경우
        if next_row == -1 or board[next_row][next_col] == 'D':
            #실제로 움직일 수 있을 때만 넣기
            if current_row != origin_row:
                next_positions.append([current_row, current_col])
            break
        current_row = next_row
        
    #하
    current_row, current_col = origin_row, origin_col
    next_col = origin_col
    while True:
        next_row = current_row +1
        #벽이나 장애물에 부딪혔을 경우
        if next_row == len(board) or board[next_row][next_col] == 'D':
            #실제로 움직일 수 있을 때만 넣기
            if current_row != origin_row:
                next_positions.append([current_row, current_col])
            break
        current_row = next_row
    
    #좌
    current_row, current_col = origin_row, origin_col
    next_row = origin_row
    while True:
        next_col = current_col-1
        #벽이나 장애물에 부딪혔을 경우
        if next_col == -1 or board[next_row][next_col] == 'D':
            #실제로 움직일 수 있을 때만 넣기
            if current_col != origin_col:
                next_positions.append([current_row, current_col])
            break
        current_col= next_col
    
    #우
    current_row, current_col = origin_row, origin_col
    next_row = origin_row
    while True:
        next_col = current_col+1
        #벽이나 장애물에 부딪혔을 경우
        if next_col == len(board[0]) or board[next_row][next_col] == 'D':
            #실제로 움직일 수 있을 때만 넣기
            if current_col != origin_col:
                next_positions.append([current_row, current_col])
            break
        current_col= next_col
    return next_positions
    

def solution(board): 
    start_row, start_col = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                start_row, start_col = i, j
    
    visited = []
    for _ in range(len(board)):
        visited.append([False]*len(board[0]))
    
    myqueue = deque()
    myqueue.append([start_row, start_col, 0])
    visited[start_row][start_col] = True
    
    #bfs
    while myqueue:
        current_row, current_col, depth = myqueue.popleft()
        if board[current_row][current_col] == 'G':
            return depth
        next_positions = get_next_positions(current_row, current_col, board)
        for position in next_positions:
            next_row, next_col = position
            if not visited[next_row][next_col]:
                myqueue.append([*position, depth+1])
                visited[next_row][next_col] = True
            
    return -1