# https://www.acmicpc.net/problem/2098
from collections import deque


def isValid(i, j, matrix):
    if matrix[i][j] == 0:
        return False
    return True


def passable(i, key):
    if (1 << i) & key:
        return False
    return True


def bfs(start_city, q, minimum_cost, matrix):
    all_visited = int('0b' + '1' * len(matrix), 2)
    while q:
        [current_city, sum_cost, key] = q.popleft()
        if key == all_visited:
            minimum_cost[0] = min(minimum_cost[0], sum_cost + matrix[current_city][start_city])

        else:
            for i, cost in enumerate(matrix[current_city]):
                if (isValid(current_city, i, matrix)
                        and passable(i, key)):
                    new_key = ((1 << i) | key)
                    new_sum_cost = sum_cost + matrix[current_city][i]
                    q.append([i, new_sum_cost, new_key])


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
minimum_cost = [1000000*16 + 1]
for i, row in enumerate(matrix):
    for j, cost in enumerate(row):
        if isValid(i, j, matrix):
            q = deque()
            key = ((1 << j) | (1 << i))
            start_city, current_city = i, j
            sum_cost = cost
            q.append([current_city, sum_cost, key])
            bfs(start_city, q, minimum_cost, matrix)

print(minimum_cost[0])


