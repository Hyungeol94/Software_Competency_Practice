# https://school.programmers.co.kr/learn/courses/30/lessons/67259
import heapq

def isValid(y, x, n):
    return 0 <= x < n and 0 <= y < n

def solution(board):
    n = len(board)
    dys = [0, 1, 0, -1]
    dxs = [1, 0, -1, 0]
    path_dirs = ['l', 'd', 'r', 'u']

    visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]  # Initialize a 3D array with infinity values
    visited[0][0] = [0, 0, 0, 0]

    pq = []  # cost, row, col, current direction
    for dy, dx, path_dir in zip(dys, dxs, path_dirs):
        if isValid(dy, dx, n) and board[dy][dx] != 1:
            visited[dy][dx][path_dirs.index(path_dir)] = 100
            heapq.heappush(pq, (100, dy, dx, path_dir))

    while pq:
        current_cost, row, col, current_dir = heapq.heappop(pq)
        if row == n - 1 and col == n - 1:
            return current_cost

        for i in range(4):
            next_row = row + dys[i]
            next_col = col + dxs[i]

            if isValid(next_row, next_col, n) and board[next_row][next_col] != 1:
                new_dir = path_dirs[i]
                cost = 100 if new_dir == current_dir else 600

                if current_cost + cost < visited[next_row][next_col][path_dirs.index(new_dir)]:
                    visited[next_row][next_col][path_dirs.index(new_dir)] = current_cost + cost
                    heapq.heappush(pq, (current_cost + cost, next_row, next_col, new_dir))

    return -1  # No path found
