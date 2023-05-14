import sys
from collections import deque

def bfs(matrix, my_queue, visited, N):
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    while my_queue:
        current_y_position, current_x_position, current_depth = my_queue.popleft()
        if matrix[current_y_position][current_x_position] == 'G':
            return current_depth

        for dy_i, dx_i in zip(dy, dx):
            next_y_position = current_y_position+dy_i
            next_x_position = current_x_position+dx_i
            next_depth = current_depth+1
            if next_y_position<0 or N <= next_y_position or next_x_position <0 or N <= next_x_position:
                continue
            if (next_y_position, next_x_position) in visited:
                continue
            if matrix[next_y_position][next_x_position] == '#':
                continue
            my_queue.append([next_y_position, next_x_position, next_depth])
            visited.add((next_y_position, next_x_position))


N = int(sys.stdin.readline().strip())
matrix = []

for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

distances = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'H':
            visited = set([(i, j)])
            my_queue = deque()
            my_queue.append([i, j, 0])
            distances.append(bfs(matrix, my_queue, visited, N))

print(max(distances)-min(distances))