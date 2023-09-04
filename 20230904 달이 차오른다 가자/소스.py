#https://www.acmicpc.net/problem/1194


from collections import deque
import copy
def passable(row, col, keys, matrix):
    if matrix[row][col].lower() in keys:
        return True
    if matrix[row][col] in '01.abcdefghijklmnopqrstuvwxyz':
        return True
    return False

def found_new_key(mark, keys):
    if mark in 'abcdefghijklmnopqrstuvwxyz' and not mark in keys:
        return True
    return False


def is_valid(next_row, next_col, matrix):
    if next_row < 0 or len(matrix) <= next_row:
        return False
    if next_col < 0 or len(matrix[0]) <= next_col:
        return False
    return True


def clear_visited(visited, row, col):
    for i, r in enumerate(visited):
        visited[i] = '0'*len(visited[0])
    check_visited(row, col, visited)
    return visited


def check_visited(row, col, visited):
    new_row = visited[row][:col] + '1' + visited[row][col + 1:] if col < len(visited[row]) else visited[row][:col] + '1'
    visited[row] = new_row

def bfs(matrix, queue, result):
    drs = [0, -1, 0, 1]
    dcs = [1, 0, -1, 0]
    while queue:
        [row, col, keys, visited, depth] = queue.popleft()
        visited = visited.split(' ')
        if matrix[row][col] == '1':
            result[0] = min(result[0], depth)
            continue

        if found_new_key(matrix[row][col], keys):
            keys = keys+matrix[row][col]
            visited = clear_visited(copy.deepcopy(visited), row, col)

        for dr, dc in zip(drs, dcs):
            next_row = row+dr
            next_col = col+dc
            if (is_valid(next_row, next_col, matrix)
                    and passable(next_row, next_col, keys, matrix)
                    and not visited[next_row][next_col] == '1'):
                check_visited(next_row, next_col, visited)
                queue.append([next_row, next_col, keys, ' '.join(visited), depth+1])

n, m = map(int, input().split())
matrix = []
visited = []
start = []
end = []
keys = ''
for i in range(n):
    matrix.append(input().strip())
    visited.append('0'*m)
    for j, mark in enumerate(matrix[i]):
        if mark == '0':
            start = [i,j]
            check_visited(i,j, visited)

start.append(keys)
start.append(' '.join(visited))
start.append(0)
queue = deque([start])
result = [25001]
bfs(matrix, queue, result)
print(result[0]) if result[0]!=25001 else print(-1)