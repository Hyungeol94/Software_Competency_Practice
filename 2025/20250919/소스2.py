#https://school.programmers.co.kr/learn/courses/30/lessons/150365
#미로 탈출 명령어

import heapq

def solution(n, m, x, y, r, c, k):
    matrix = [["." for _ in range(m)] for _ in range(n)]
    drs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    marks = ["d", "l", "r", "u"]
    
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, (0, "", x-1, y-1))
    seen = set()
    seen.add((0, x-1, y-1))
    while heap:
        depth, path, i, j = heapq.heappop(heap)
        depth = -depth
        
        if depth == k and i == r-1 and j == c-1:
            return path
        
        if depth == k:
            continue
            
        for dr, mark in zip(drs, marks):
            i_offset, j_offset = dr
            next_i = i+i_offset
            next_j = j+j_offset
            if not (0 <= next_i < n and 0 <= next_j < m): 
                continue
            if (depth+1, next_i, next_j) in seen:
                continue
            heapq.heappush(heap, (-(depth+1), path+mark, next_i, next_j))
            seen.add((depth+1, next_i, next_j))
    
    return "impossible"