#https://school.programmers.co.kr/learn/courses/30/lessons/161988#
#연속 펄스 부분 수열의 합

def solution(sequence):
    seq1 = []
    seq2 = []
    for i, num in enumerate(sequence):
        if i % 2 == 0:
            seq1.append(num)
            seq2.append(0 - num)
        else:
            seq1.append(0 - num)
            seq2.append(num)

    seq1_prefixes = []
    seq2_prefixes = []
    
    acc = 0
    for i, num in enumerate(seq1):
        acc += num
        seq1_prefixes.append(acc)
    
    acc = 0
    for i, num in enumerate(seq2):
        acc += num
        seq2_prefixes.append(acc)
    

    minVal = float('inf')
    maxVal = -float('inf')
    for num in seq1_prefixes:
        minVal = min(minVal, num)
        maxVal = max(num-minVal, maxVal, num)
    
    minVal = float('inf')
    for num in seq2_prefixes:
        minVal = min(minVal, num)
        maxVal = max(num-minVal, maxVal, num)
    
    return maxVal