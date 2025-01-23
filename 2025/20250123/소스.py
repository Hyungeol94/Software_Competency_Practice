#https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23
#Count Servers that Communicate

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counts = []
        col_counts = []

        for row in grid:
            row_counts.append(sum(row))
        
        for col in zip(*grid):
            col_counts.append(sum(col))
        
        count = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if not grid[i][j]:
                    continue
                if 2 <= row_counts[i] or 2 <= col_counts[j]:
                    count += 1
        return count