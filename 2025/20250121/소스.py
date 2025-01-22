#https://leetcode.com/problems/grid-game/description/
#2017. Grid Game

from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        #minimize maximum
        #what is its minimized maximum? 
        #그림에서 힌트 얻음
        upper_acc = sum(grid[0]) - grid[0][0]
        lower_acc = 0
        minimized_maximum = max(upper_acc, lower_acc)

        for i in range(1, n):
            upper_acc -= grid[0][i]
            lower_acc += grid[1][i-1]
            minimized_maximum = min(minimized_maximum, max(upper_acc, lower_acc))
        return minimized_maximum