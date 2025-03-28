#https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description/?envType=daily-question&envId=2025-03-28
#2503. Maximum Number of Points From Grid Queries

from collections import deque
from collections import defaultdict
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        #bfs를 한번만 하고 값을 저장
        #query를 정렬
        sorted_queries = sorted(queries)
        k = len(queries)
        drs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        visited = [[False]*m for _ in range(n)]
        visited[0][0] = True
        query_results = defaultdict(int)
        i = 0
        while i < k and sorted_queries[i] <= grid[0][0]: #점수를 얻기 위해서는 커야 함
            i += 1

        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, [grid[0][0], 0, 0]) 

        acc_score = 0
        while i < k:
            myqueue = deque([])
            while heap:
                score, row, col = heap[0]
                if  score < sorted_queries[i]:
                    myqueue.append([row, col])
                    visited[row][col] = True
                    heapq.heappop(heap)
                    continue
                else:
                    break

            while myqueue:
                row, col = myqueue.popleft()
                acc_score += 1
                for row_offset, col_offset in drs:
                    next_row, next_col = row+row_offset, col+col_offset
                    if not (0 <= next_row < n and 0 <= next_col < m):
                        continue
                    if visited[next_row][next_col]:
                        continue
                    if not grid[next_row][next_col] < sorted_queries[i]:
                        visited[next_row][next_col] = True
                        heapq.heappush(heap, [grid[next_row][next_col], next_row, next_col]) #다음을 위해
                        continue

                    myqueue.append([next_row, next_col])
                    visited[next_row][next_col] = True
            
            query_results[sorted_queries[i]] = acc_score
            i += 1
        
        answer = []
        for query in queries:
            answer.append(query_results[query])
        return answer