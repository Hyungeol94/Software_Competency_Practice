import heapq
from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        #minimize maximum -> binary search
        #what is its minimized maximum ?? 
        upper_acc = sum(grid[0]) - grid[0][0]
        lower_acc = 0
        minimized_maximum = max(upper_acc, lower_acc)

        for i in range(1, n):
            upper_acc -= grid[0][i]
            lower_acc += grid[1][i-1]
            minimized_maximum = min(minimized_maximum, max(upper_acc, lower_acc))
        return minimized_maximum