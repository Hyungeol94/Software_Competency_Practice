import sys
from queue import PriorityQueue

def calculate_distance(x, y, hubs):
    distance = 1000000000
    for i, j in hubs:
        this_distance = abs(i-x)+abs(j-y)
        distance = min(this_distance, distance)
    return distance

def bfs(matrix, my_queue, visited, N, distances, hubs):
    #빠르게 최소 거리를 찾을 수 있는 방법 -> Prority_Queue를 이용

    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]
    while my_queue:
        current_distance, current_y_position, current_x_position, current_depth = my_queue.get()
        if matrix[current_y_position][current_x_position] == 'G':
            distances[0] = min(current_depth, distances[0])
            distances[1] = max(current_depth, distances[1])
            return current_depth

        for dy_i, dx_i in zip(dy, dx):
            next_y_position = current_y_position + dy_i
            next_x_position = current_x_position + dx_i
            next_depth = current_depth + 1
            if next_y_position < 0 or N <= next_y_position or next_x_position < 0 or N <= next_x_position:
                continue
            if (next_y_position, next_x_position) in visited:
                continue
            if matrix[next_y_position][next_x_position] == '#':
                continue
            next_distance = calculate_distance(next_y_position, next_x_position, hubs)
            my_queue.put([next_distance, next_y_position, next_x_position, next_depth])
            visited.add((next_y_position, next_x_position))


N = int(sys.stdin.readline().strip())
matrix = []
hubs = []
for i in range(N):
    matrix.append(sys.stdin.readline().strip())
    for j in range(N):
        if matrix[i][j] == 'G':
            hubs.append([i, j])

distances = [1000000000, -1]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'H':
            visited = set([(i, j)])
            my_queue = PriorityQueue()
            this_distance = calculate_distance(i, j, hubs)
            my_queue.put([this_distance, i, j, 0])
            bfs(matrix, my_queue, visited, N, distances, hubs)

# print(max(distances)-min(distances))
print(distances[1] - distances[0])