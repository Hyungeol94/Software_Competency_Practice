#https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/?envType=daily-question&envId=2025-05-07
#3341. Find Minimum Time to Reach Last Room I

import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        heap = []
        heapq.heapify(heap)
        drs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        heapq.heappush(heap, (0, 0, 0))

        #다익스트라 알고리즘
        dp = [[float('inf')]*m for _ in range(n)]
        dp[0][0] = 0

        while heap:
            curr = heapq.heappop(heap)
            time, row, col = curr
            for dr in drs:
                next_row = row + dr[0]
                next_col = col + dr[1]
                if not (0 <= next_row < n and 0 <= next_col < m): #범위확인
                    continue
                next_time = moveTime[next_row][next_col]+1
                if next_time < time + 1:
                    next_time = time+1
                print(next_time, next_row, next_col)
                if next_time < dp[next_row][next_col]:
                    dp[next_row][next_col] = next_time
                    heapq.heappush(heap, (next_time, next_row, next_col))
            
        
        return dp[n-1][m-1]