#https://leetcode.com/problems/equal-sum-grid-partition-i/?envType=daily-question&envId=2026-03-25
#3546. Equal Sum Grid Partition I

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        row_prefixes, row_suffixes = [], []
        acc = 0
        for row in grid:
            acc += sum(row)
            row_prefixes.append(acc)
        
        acc = 0
        for row in reversed(grid):
            acc += sum(row)
            row_suffixes.append(acc)
        
        row_suffixes = row_suffixes[::-1]

        for i in range(n-1):
            prefix = row_prefixes[i]
            suffix = row_suffixes[i+1]
            if prefix == suffix:
                return True

        col_prefixes, col_suffixes = [], []
        acc = 0
        for col in zip(*grid):
            acc += sum(col)
            col_prefixes.append(acc)
        
        acc = 0
        for col in reversed(list(zip(*grid))):
            acc += sum(col)
            col_suffixes.append(acc)
        
        col_suffixes = col_suffixes[::-1]

        for i in range(m-1):
            prefix = col_prefixes[i]
            suffix = col_suffixes[i+1]
            if prefix == suffix:
                return True
        
        return False