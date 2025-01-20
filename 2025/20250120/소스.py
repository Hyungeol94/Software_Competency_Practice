from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        positions = {}
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                positions[mat[i][j]] = (i, j)
        
        row_counts: List[int] = [n] * m
        col_counts: List[int] = [m] * n

        for i, num in enumerate(arr):
            row, col = positions[num]
            row_counts[row] -= 1
            col_counts[col] -= 1
            if row_counts[row] == 0 or col_counts[col] == 0:
                return i