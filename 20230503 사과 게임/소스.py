import sys
def sum_is_ten(matrix, p, q, i, j):
    sum_elements = 0
    for k in range(i, i+p+1):
        for z in range(j, j+q+1):
            sum_elements += matrix[k][z]
    if sum_elements == 10:
        return True
    return False

def check(p,q, matrix, N, M):
    #matrix 안에 p, q 크기의 직사각형으로 몇 개의 10을 만들 수 있는지 return 하기
    square_making_ten = 0
    for i in range(0, N-p):
        for j in range(0, M-q):
            if sum_is_ten(matrix, p, q, i, j):
                square_making_ten += 1
    return square_making_ten

N,M = list(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

answer = 0
#가능한 모든 직사각형의 크기
for i in range(N):
    for j in range(M):
        answer += check(i,j,matrix, N, M)

print(answer)