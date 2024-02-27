#https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]

        if n == 1:
            return matrix[0][0]

        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][0], dp[i-1][1])+matrix[i][0]
            dp[i][n-1] = min(dp[i-1][n-2], dp[i-1][n-1])+matrix[i][n-1]
            if 2<n:
                for j in range(1, n-1):
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
            
        return min(dp[n-1])

    
