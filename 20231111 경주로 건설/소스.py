#https://school.programmers.co.kr/learn/courses/30/lessons/67259	
import heapq
from copy import deepcopy

def isValid(y, x, n):
    if 0<=x<=n-1 and 0<=y<=n-1:
        return True
    return False

def markAsVisited(visited, row, col):
    visited[row]  = (visited[row] | (1 << col))
    
def isVisited(visited, row, col): 
    if (visited[row] & (1 << col)):
        return True
    return False

def solution(board):
    n = len(board)
    dys = [0, 1, 0, -1]
    dxs = [1, 0, -1, 0]
    path_dirs = ['l', 'd', 'r', 'u']
    visited = [0]*n
    markAsVisited(visited, 0, 0)
    
    pq = [] # 비용, 방향, 방문
    for dy, dx, path_dir in zip(dys, dxs, path_dirs):
        if isValid(dy, dx, n) and not board[dy][dx] == 1:
            new_visited = deepcopy(visited)
            markAsVisited(new_visited, dy, dx)
            heapq.heappush(pq, [100, path_dir, visited, dy, dx])
    
    while pq:
        current_cost, current_path_dir, visited, row, col= heapq.heappop(pq)
        print(current_cost)
        if row == n-1 and col == n-1:
            return current_cost
        for dx, dy, path_dir in zip(dxs, dys, path_dirs):
            next_row = row+dy
            next_col = col+dx
            cost = 100 if path_dir == current_path_dir else 500
            if isValid(next_row, next_col, n) and not isVisited(visited, next_row, next_col) and not board[next_row][next_col]==1:
                new_visited = deepcopy(visited)
                markAsVisited(new_visited, next_row, next_col)
                heapq.heappush(pq, [current_cost+cost, path_dir, visited, next_row, next_col])