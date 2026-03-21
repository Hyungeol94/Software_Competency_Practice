#https://leetcode.com/problems/flip-square-submatrix-vertically/?envType=daily-question&envId=2026-03-21
#3643. Flip Square Submatrix Vertically

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(x, x + k // 2):
            for j in range(y, y+k):
                grid[i][j], grid[x+k-1-(i-x)][j] = grid[x+k-1-(i-x)][j], grid[i][j]
        return grid