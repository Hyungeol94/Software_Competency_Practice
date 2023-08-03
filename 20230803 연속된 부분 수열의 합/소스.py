#https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):    
    matrix = []
    for i in range(len(sequence)):
        matrix.append([0]*len(sequence))
        matrix[i][i] = sequence[i]
        if matrix[i][i] == k:
            return [i, i]
    
    shift = 1
    while shift != len(sequence):
        for i in range(len(sequence)):
            start = i
            end = start+shift
            if end == len(sequence):
                break            
            matrix[start][end] = matrix[start][end-1]+sequence[end]
            if matrix[start][end] == k:
                return [start, end]
        shift += 1 
        
            
        
            def solution(sequence, k):    
    matrix = []
    for i in range(len(sequence)):
        matrix.append([0]*len(sequence))
        matrix[i][i] = sequence[i]
        if matrix[i][i] == k:
            return [i, i]
    
    shift = 1
    while shift != len(sequence):
        for i in range(len(sequence)):
            start = i
            end = start+shift
            if end == len(sequence):
                break            
            matrix[start][end] = matrix[start][end-1]+sequence[end]
            if matrix[start][end] == k:
                return [start, end]
        shift += 1 
        
            
        
            