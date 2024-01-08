#https://www.acmicpc.net/problem/1194

from collections import deque
import copy
def passable(row, col, keys, matrix):
    if matrix[row][col] == '#':
        return False
    elif matrix[row][col] in '.01':
        return True
    elif 'a' <= matrix[row][col] <= 'f':
        return True
    elif bitmask(matrix[row][col].lower()) & keys:
        return True
    return False


def found_new_key(mark, keys):
    if mark in 'abcdef' and not (bitmask(mark) & keys):
        return True
    return False


def is_valid(next_row, next_col, matrix):
    if next_row < 0 or len(matrix) <= next_row:
        return False
    if next_col < 0 or len(matrix[0]) <= next_col:
        return False
    return True


def bitmask(key):
    return 1 << (ord(key)-ord('a'))


def bfs(matrix, visited, queue, result):
    drs = [0, -1, 0, 1]
    dcs = [1, 0, -1, 0]

    while queue:
        [row, col, depth, keys] = queue.popleft()
        if matrix[row][col] == '1':
            result[0] = min(result[0], depth)
        if found_new_key(matrix[row][col], keys):
            keys = bitmask(matrix[row][col]) | keys
            visited[keys][row][col] = True

        for dr, dc in zip(drs, dcs):
            next_row = row+dr
            next_col = col+dc
            if (is_valid(next_row, next_col, matrix)
                    and not visited[keys][next_row][next_col]
                    and passable(row, col, keys, matrix)):
                queue.append([next_row, next_col, depth+1, keys])
                visited[keys][next_row][next_col] = True


n, m = map(int, input().split())
matrix = []
start = []
end = []
keys = 0
visited = [[[False]*m for _ in range(n)] for _ in range(64)]

for i in range(n):
    matrix.append(input().strip())
    for j, mark in enumerate(matrix[i]):
        if mark == '0':
            start = [i,j]
            visited[keys][i][j] = True

start.append(0)
start.append(keys)
queue = deque([start])
result = [25001]
bfs(matrix, visited, queue, result)
print(result[0]) if result[0]!=25001 else print(-1)