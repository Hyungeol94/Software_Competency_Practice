#https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    matrix = [1 for _ in range(n)]
    lost.sort()
    reserve.sort()
    for i in lost:
        if not i in reserve:
            matrix[i-1] = 0
        
    for i in reserve:
        if i in lost:
            continue
        if i-2 >=0 and matrix[i-2] == 0:
            matrix[i-2] = 1
            continue
        if i <= n-1 and matrix[i] == 0:
            matrix[i] =  1
    return matrix.count(1)