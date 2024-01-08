#https://school.programmers.co.kr/learn/courses/30/lessons/120866

def is_valid(number, limit):
    if number < 0 or limit <= number:
        return False
    return True


def indicate(matrix, point):
    i, j = point
    d_rows = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    d_cols = [0, 1, 1, 0, -1, -1, -1, 0, 1]
    for d_row, d_col in zip(d_rows, d_cols):
        next_row, next_col = i+d_row, j+d_col
        if is_valid(next_row, len(matrix)) and is_valid(next_col, len(matrix)):
            matrix[next_row][next_col] = True


def solution(board):
    matrix = [[False] * len(board) for _ in range(len(board))]
    for i, row in enumerate(board):
        for j, mark in enumerate(row):
            if mark == 1:
                point = [i, j]
                indicate(matrix, point)

    count = 0
    for row in matrix:
        count += row.count(False)

    return count