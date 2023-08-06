# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def get(x, y, matrix, sequence):
    if matrix[x][y] == 0:
        matrix[x][y] = get(x, y-1, matrix, sequence) + sequence[y]
    return matrix[x][y]

def solution(sequence, k):
    matrix = []
    for i in range(len(sequence)):
        matrix.append([0] * len(sequence))
        matrix[i][i] = sequence[i]
        if matrix[i][i] == k:
            return [i, i]

    left = 0
    right = 0
    candidates = []
    while not(left == len(sequence)-1 and right == len(sequence)-1):
        while right != len(sequence):
            subsequence_sum = get(left, right, matrix, sequence)
            if subsequence_sum < k:
                right += 1
            if subsequence_sum > k:
                break
            if subsequence_sum == k:
                candidates.append([left, right])
                break
        left += 1
        right = left

    candidates.sort(key=lambda a: (abs(a[1]-a[0])))
    
    return candidates[0]






