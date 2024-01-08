#6846. 그림 곱하기
#입력으로 그림이 하나 주어집니다. 1 이상의 정수를 한 번 곱해서 이 그림을 만들 수 있는 그림들 중 그 넓이가 가장 작은것을 출력하는 프로그램을 작성해 주세요.

import sys
def is_identical(row_length, column_length, matrix, row_point, column_point):
    for i in range(row_length):
        for j in range(column_length):
            if matrix[i][j] != matrix[row_point + i][column_point + j]:
                return False
    return True

def check(row_length, column_length, matrix, N, M):
#전체 다 체크
    for i in range(1, N//row_length):
        for j in range(1, M//column_length):
            if not is_identical(row_length, column_length, matrix, row_length*i, column_length*j):
                return False
    return True

def print_matrix(row_length, column_length, matrix):
    for i in range(row_length):
        for j in range(column_length):
            print(matrix[i][j], end = '')
        if i != row_length-1:
            print()

(N, M) = list(map(int, sys.stdin.readline().split()))
#공통으로 나눌 수 있는 수 있는 수를 찾아야 함..
matrix = []
for _ in range(N):
    matrix.append(sys.stdin.readline().strip())

MAX_NUMBER = min(N,M)
FOUND = False
for i in range(MAX_NUMBER, 1, -1):
    if N % i == 0 and M % i == 0:
        row_length = N // i
        column_length  = M // i
        if check(row_length, column_length, matrix, N, M):
            print_matrix(row_length, column_length, matrix)
            FOUND = True
            break

if not FOUND:
    print_matrix(N, M, matrix)