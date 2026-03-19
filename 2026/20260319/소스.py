#https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/?envType=daily-question&envId=2026-03-19
#3212. Count Submatrices With Equal Frequency of X and Y

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dp_x = [[0]*m for _ in range(n)]
        dp_y = [[0]*m for _ in range(n)]

        dp_x[0][0] = 1 if grid[0][0] == 'X' else 0
        dp_y[0][0] = 1 if grid[0][0] == 'Y' else 0
        
        for i in range(1, n):
            dp_x[i][0] = dp_x[i-1][0] + 1 if grid[i][0] == 'X' else dp_x[i-1][0]
            dp_y[i][0] = dp_y[i-1][0] + 1 if grid[i][0] == 'Y' else dp_y[i-1][0]
        
        for j in range(1, m):
            acc_x = 0
            acc_y = 0
            for i in range(n):
                acc_x += 1 if grid[i][j] == 'X' else 0
                acc_y += 1 if grid[i][j] == 'Y' else 0
                dp_x[i][j] = dp_x[i][j-1] + acc_x
                dp_y[i][j] = dp_y[i][j-1] + acc_y
                
        count = 0
        for i in range(n):
            for j in range(m):
                if dp_x[i][j] < 1:
                    continue        
                if dp_x[i][j] != dp_y[i][j]:
                    continue
                count += 1
        
        return count
        