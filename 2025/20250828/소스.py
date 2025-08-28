#https://leetcode.com/problems/sort-matrix-by-diagonals/?envType=daily-question&envId=2025-08-28
#3446. Sort Matrix by Diagonals

import heapq

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        if n == 1:
            return grid

        #left-bottom triangle 먼저 처리
        k = n-1
        while k >= 0:
            i = k
            j = 0
            #정렬하며 이동
            myheap = []
            heapq.heapify(myheap)
            while i < n:
                heapq.heappush(myheap, -grid[i][j])
                i += 1
                j += 1

            #재정렬해서 넣기
            i = k
            j = 0
            while i < n:
                curr = heapq.heappop(myheap)
                grid[i][j] = -curr
                i += 1
                j += 1
            k -= 1 

        #top-right triangle 처리
        k = 1
        while k < n:
            i = 0
            j = k
            myheap = []
            while j < n:
                heapq.heappush(myheap, grid[i][j])
                i += 1
                j += 1
            i = 0
            j = k
            while j < n:
                curr = heapq.heappop(myheap)
                grid[i][j] = curr
                i += 1
                j += 1
            k += 1

        return grid