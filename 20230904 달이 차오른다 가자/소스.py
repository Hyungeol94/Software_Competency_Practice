#https://www.acmicpc.net/problem/1194

from collections import deque

def passable(row, col, keys, matrix):
    if matrix[row][col].lower() in keys:
        return True
    if matrix[row][col] in '01.abcdef':
        return True
    return False

def found_new_key(mark, keys):
    if mark in 'abcdef' and not mark in keys:
        return True
    return False


def is_valid(next_row, next_col, matrix):
    if next_row < 0 or len(matrix) <= next_row:
        return False
    if next_col < 0 or len(matrix[0]) <= next_col:
        return False
    return True


def bfs(matrix, visited, queue, result):
    drs = [0, -1, 0, 1]
    dcs = [1, 0, -1, 0]

    while queue:
        [row, col, depth, keys] = queue.popleft()
        if matrix[row][col] == '1':
            result[0] = min(result[0], depth)

        if found_new_key(matrix[row][col], keys):
            keys = sorted(keys+[matrix[row][col]])
            visited[''.join(keys)] = []
            for _ in range(len(matrix)):
                visited[''.join(keys)].append([False]*len(matrix[0]))
            visited[''.join(keys)][row][col] = True

        for dr, dc in zip(drs, dcs):
            next_row = row+dr
            next_col = col+dc
            if (is_valid(next_row, next_col, matrix)
                    and passable(next_row, next_col, keys, matrix)
                    and not visited[''.join(keys)][next_row][next_col]):
                queue.append([next_row, next_col, depth+1, keys])
                visited[''.join(keys)][next_row][next_col] = True


n, m = map(int, input().split())
matrix = []
start = []
end = []
keys = []
visited = {}
visited[''.join(keys)] = []
for i in range(n):
    matrix.append(input().strip())
    visited[''.join(keys)].append([False]*m)
    for j, mark in enumerate(matrix[i]):
        if mark == '0':
            start = [i,j]
            visited[''.join(keys)][i][j] = True

start.append(0)
start.append(keys)
queue = deque([start])
result = [25001]
bfs(matrix, visited, queue, result)
print(result[0]) if result[0]!=25001 else print(-1)