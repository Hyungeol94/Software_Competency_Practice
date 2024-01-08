import sys
from copy import deepcopy

def is_winning(matrix, row, col):
    #(row, col)을 바꿨는데, matrix 상에서 이기는 수인지 확인
    if lateral_check(matrix, row, col) or vertical_check(matrix, row, col) or diagonal_check(matrix, row, col):
        return True
    return False

def lateral_check(matrix, row, col):
    count = 1
    #왼쪽으로 이동
    origin_row, origin_col = row, col
    while col != 0:
        col -= 1
        if matrix[row][col] == 'W':
            count += 1
            continue;
        break

    row, col = origin_row, origin_col
    #오른쪽으로 이동
    while col != 9:
        col += 1
        if matrix[row][col] == 'W':
            count += 1
            continue
        break

    if count >= 5:
        return True
    return False

def vertical_check(matrix, row, col):
    count = 1
    origin_row, origin_col = row, col
   #위쪽으로 이동
    while row != 0:
        row -= 1
        if matrix[row][col] == 'W':
            count += 1
            continue;
        break

    # 아래쪽으로 이동
    row, col = origin_row, origin_col
    while row != 9:
        row += 1
        if matrix[row][col] == 'W':
            count += 1
            continue
        break

    if count >= 5:
        return True
    return False

def diagonal_check(matrix, row, col):
    count = 1
    origin_row, origin_col = row, col
    # 왼쪽 위로 이동
    while row != 0 and col != 0:
        row -= 1
        col -= 1
        if matrix[row][col] == 'W':
            count += 1
            continue;
        break

    # 오른쪽 아래로 이동
    row, col = origin_row, origin_col
    while row != 9 and col != 9:
        row += 1
        col += 1
        if matrix[row][col] == 'W':
            count += 1
            continue
        break

    if count >= 5:
        return True
    return False


def lateral_erase(matrix, row):
    matrix[row] = '.'*10

def vertical_erase(matrix, col):
    if col != 9:
        for i in range(10):
            matrix[i] = matrix[i][:col] + '.' + matrix[i][col+1:]
    if col == 9:
        for i in range(10):
            matrix[i] = matrix[i][:col] + '.'

matrix = []
for _ in range(10):
    char_string = sys.stdin.readline().strip()
    matrix.append(char_string)

count = 0
for i in range(10):
    for j in range(10):
        if matrix[i][j] != '.':
            temp_matrix = deepcopy(matrix)
            lateral_erase(temp_matrix, i)
            if is_winning(temp_matrix, i, j):
                count += 1

for i in range(10):
    for j in range(10):
        if matrix[i][j] != '.':
            temp_matrix = deepcopy(matrix)
            vertical_erase(temp_matrix, j)
            if is_winning(temp_matrix, i, j):
                count += 1

print(count)

