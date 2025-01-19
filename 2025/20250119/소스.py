#https://leetcode.com/problems/trapping-rain-water-ii/description/
#407. Trapping Rain Water II

from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])

        #matrix 초기화
        matrix: List[List[int]] = [[0]*m for _ in range(n)]
        visited: List[List[bool]] = [[False]*m for _ in range(n)]

        #다익스트라 응용
        heap = []
        heapq.heapify(heap)
        
        #가장 바깥쪽에서부터 시작
        for i in range(n):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][-1], i, m-1))
            visited[i][0] = True
            visited[i][-1] = True
        
        for j in range(m):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[-1][j], n-1, j))
            visited[0][j] = True
            visited[-1][j] = True
        
        drs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            #높이가 제일 낮은 곳부터 나옴
            #neighbor cell의 height에 비교되는 height가, 비교가능한 높이들 중 가장 최소값임이 보장됨
            curr_height, row, col = heapq.heappop(heap)
            for row_offset, col_offset in drs:
                next_row = row+row_offset
                next_col = col+col_offset
                if not (0 <= next_row < n and 0 <= next_col < m):
                    continue
                if visited[next_row][next_col]: 
                    continue
                neighbor_height = heightMap[next_row][next_col]
                if neighbor_height < curr_height:
                    matrix[next_row][next_col] = curr_height-neighbor_height
                    heapq.heappush(heap, (curr_height, next_row, next_col))
                else:
                    heapq.heappush(heap, (neighbor_height, next_row, next_col))
                #visit 처리를 통해 중복 탐색 방지
                visited[next_row][next_col] = True    
            
        acc = 0
        for row in matrix:
            acc += sum(row)
        return acc