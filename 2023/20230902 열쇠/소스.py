#https://www.acmicpc.net/problem/9328

from collections import deque


def passable(mark, keys):
    if (mark in '.$abcdefghijklmnopqrstuvwxyz') or mark.lower() in keys:
        return True
    return False


def is_valid(number, matrix, mark):
    if mark == 'r':
        if number < 0 or len(matrix) <= number:
            return False
        return True

    if mark == 'c':
        if number < 0 or len(matrix[0]) <= number:
            return False
        return True


def found_new_key(point, keys):
    if point in 'abcdefghijklmnopqrstuvwxyz' and not (point in keys):
        return True
    return False


def bfs(starting_points, matrix, keys):
    myqueue = deque(starting_points)
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    d_row = [0, -1, 0, 1]
    d_col = [1, 0, -1, 0]

    point = 0
    for [row, col] in starting_points:
        myqueue.append([row, col])
        if not visited[row][col] and matrix[row][col] == '$':
            point += 1
        visited[row][col] = True
        if found_new_key(matrix[row][col], keys):
            keys.append(matrix[row][col])
            starting_points = get_starting_points(matrix, keys)
            return bfs(starting_points, matrix, keys)


    while myqueue:
        current_position = myqueue.popleft()
        row, col = current_position
        for dr, dc in list(zip(d_row, d_col)):
            next_row, next_col = row+dr, col+dc
            if is_valid(next_row, matrix, 'r') and is_valid(next_col, matrix, 'c') and not visited[next_row][next_col]:
                #열쇠를 찾음 ->키를 추가하고, 처음부터 가지고 있다고 생각하며 bfs 새로 시작
                if found_new_key(matrix[next_row][next_col], keys):
                    keys.append(matrix[next_row][next_col])
                    starting_points = get_starting_points(matrix, keys)
                    return bfs(starting_points, matrix, keys)
                if passable(matrix[next_row][next_col], keys):
                    myqueue.append([next_row, next_col])
                    if matrix[next_row][next_col] == '$':
                        point += 1
                    visited[next_row][next_col] = True
    return point


def get_starting_points(matrix, keys):
    starting_points = []
    for j, mark in enumerate(matrix[0]):
        if passable(mark, keys):
            starting_points.append([0, j])

    for j, mark in enumerate(matrix[-1]):
        if passable(mark, keys):
            starting_points.append([len(matrix)-1, j])

    for j, mark in enumerate(list(zip(*matrix))[0][1:-1]):
        if passable(mark, keys):
            starting_points.append([j+1, 0])

    for j, mark in enumerate(list(zip(*matrix))[-1][1:-1]):
        if passable(mark, keys):
            starting_points.append([j+1, len(list(zip(*matrix)))-1])
    return starting_points


def compute():
    h, w = map(int, input().split())
    matrix = []
    for i in range(h):
        matrix.append(input().strip())
    keys = list(input().strip())
    starting_points = get_starting_points(matrix, keys)
    visited = [[False]*w for _ in range(h)]
    point = bfs(starting_points, matrix, keys)
    print(point)


T = int(input().strip())
for _ in range(T):
    compute()
