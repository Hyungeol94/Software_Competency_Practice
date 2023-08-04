#https://school.programmers.co.kr/learn/courses/30/lessons/178870

def get(x, y, matrix, sequence):
    if matrix[x][y] == 0:
        matrix[x][y] = get(x, y-1, matrix, sequence) + sequence[y]
    return matrix[x][y]

def find(start, end, k, matrix, sequence):
    lux, luy = start
    rdx, rdy = end
    middle = (lux+rdx)//2, (luy+rdy)//2
    x, y = middle
    if get(x, y, matrix, sequence) == k:
        return [x, y]
    if (lux == x and luy == y) and (get(x, y, matrix, sequence) != k):
        return False
    return find(start, middle, k, matrix, sequence) if matrix[x][y] > k else find(middle, end, k, matrix, sequence)

def search_value(matrix, value, k, sequence):
    x, y = value
    while(x != 0):
        x-= 1
        y-= 1
    while(x != len(matrix)-1):
        if get(x, y, matrix, sequence) == k:
            return [x, y]
        x += 1
        y += 1




def solution(sequence, k):
    matrix = [[0 for _ in range(len(sequence))] for _ in range(len(sequence))]
    for i in range(len(sequence)):
        matrix[i][i] = sequence[i]
        if matrix[i][i] == k:
            return [i, i]

    shift = 1
    while shift != len(sequence):
        if shift > k:
            break
        start = (0, shift)
        end = (len(sequence)-1-shift, len(sequence)-1)
        value = find(start, end, k, matrix, sequence)
        if value:
            #return value
            return search_value(matrix, value, k, sequence)
        shift += 1




