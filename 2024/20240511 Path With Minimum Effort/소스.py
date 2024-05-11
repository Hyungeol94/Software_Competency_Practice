import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def isValid(row, col):
            if 0 <= row <= len(heights)-1 and 0 <= col <= len(heights[0])-1:
                return True
            return False
        
        dxs = [0, 1, 0, -1]
        dys = [-1, 0, 1, 0]

        efforts = [[float('inf')]*len(heights[0]) for _ in range(len(heights))]

        myqueue = [[0, 0, 0]]
        heapq.heapify(myqueue)
        while myqueue:
            effort, row, col = heapq.heappop(myqueue)
            if row == len(heights)-1 and col == len(heights[0])-1:
                return effort

            for dx, dy in zip(dxs, dys):
                next_row = row+dy
                next_col = col+dx
                
                if isValid(next_row, next_col):
                    if abs(heights[row][col]-heights[next_row][next_col]) < efforts[next_row][next_col]:
                        next_effort = max(effort, abs(heights[row][col]-heights[next_row][next_col]))
                        heapq.heappush(myqueue, [next_effort, next_row, next_col])
                        efforts[next_row][next_col] = abs(heights[row][col]-heights[next_row][next_col])
                