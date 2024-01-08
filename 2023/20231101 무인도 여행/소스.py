#https://school.programmers.co.kr/learn/courses/30/lessons/154540?language=python3

from collections import deque


def is_valid(i, j, maps):
    if not (0 <= i <= len(maps)-1 and 0 <= j <= len(maps[0])-1):
        return False
    if maps[i][j] == 'X':
        return False
    return True


def bfs(q, maps, visited):
    d_rows = [1, 0, -1, 0]
    d_cols = [0, 1, 0, -1]
    count = 0
    while q:
        [i, j] = q.popleft()
        count += int(maps[i][j])
        for [d_row, d_col] in zip(d_rows, d_cols):
            next_row = i+d_row
            next_col = j+d_col
            if is_valid(next_row, next_col, maps):
                if not (visited[next_row] & (1 << next_col)):
                    visited[next_row] = visited[next_row] | (1 << next_col)
                    q.append([next_row, next_col])

    return count


def solution(maps):
    visited = [0] * len(maps)
    answer = []
    for i, row in enumerate(maps):
        for j, item in enumerate(row):
            if item != 'X' and not (visited[i] & (1 << j)):
                visited[i] = visited[i] | (1 << j)
                q = deque([[i, j]])
                answer.append(bfs(q, maps, visited))

    return sorted(answer) if answer else [-1]
