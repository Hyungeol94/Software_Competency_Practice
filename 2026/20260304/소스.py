#https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2026-03-04
#1582. Special Positions in a Binary Matrix

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_bins = list(map(lambda a: int("0b"+"".join(map(str, a)), 2), mat))
        col_bins = list(map(lambda a: int("0b"+"".join(map(str, a)), 2), list(zip(*mat))))
        
        n, m = len(mat), len(mat[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if not mat[i][j] == 1:
                    continue
                if row_bins[i].bit_count() == 1 and col_bins[j].bit_count() == 1:
                    count += 1
        return count 