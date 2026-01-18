#https://leetcode.com/problems/largest-magic-square/?envType=daily-question&envId=2026-01-18
#1895. Largest Magic Square

from typing import List

class Solution:
    def checkSquare(self, grid, i, j, k):
        #기준값 찾기
        sum_val = sum(grid[i][j:j+k])

        #각 행 확인
        for row_offset in range(k):
            if sum(grid[i+row_offset][j:j+k]) != sum_val:
                return False
        
        #각 열 확인
        for col_offset in range(k):
            if sum(map(lambda row: row[j+col_offset], grid[i:i+k])) != sum_val:
                return False 

        #대각선1 확인
        acc = 0
        for offset in range(k):
            acc += grid[i+offset][j+offset]
        if acc != sum_val:
            return False
        
        #대각선2 확인
        acc = 0
        for offset in range(k):
            acc += grid[i+offset][j+k-1-offset]
        if acc != sum_val:
            return False
        return True

    
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        #최대 50
        #O(n^2) => 2500
        #1회 탐색에 n만큼 소요 => 125000
        
        n = len(grid)
        m = len(grid[0])
        upper_bound = min(n, m)
        lower_bound = 1
        for k in range(upper_bound, lower_bound-1, -1):
            for i in range(n):
                for j in range(m):
                    if not (0 <= i+k-1 < n and 0<= j+k-1 < m):
                        continue
                    if self.checkSquare(grid, i, j, k):
                        return k
        
        return 1