class Solution:
    def isValid(self, n, i, j):
        if 0 <= i <= n-1 and 0 <= j <= n-1:
            return True
        return False
    
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        if n == 1:
            return dp[0][0]
        
        for i in range(1, n):
            for j in range(n):
                prev_row = i-1
                for prev_col in range(n):
                    if prev_col == j:
                        continue
                    if not self.isValid(n, prev_row, prev_col):
                        continue
                    dp[i][j] = min(dp[i][j], dp[prev_row][prev_col]+grid[i][j])
        
        return min(dp[n-1])


                
                